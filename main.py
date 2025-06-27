import os
import logging
import random
import json
import time
from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from utils.dialogflow_utils import get_dialogflow_response
from utils.image_utils import generate_waifu_image
from utils.voice_utils import generate_waifu_voice
from utils.memory_utils import save_conversation, get_user_profile
from config import TELEGRAM_TOKEN, DIALOGFLOW_PROJECT_ID

# Configuração de logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Carregar personalidade
with open('kaoruko_personality.json', 'r', encoding='utf-8') as f:
    PERSONALITY = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    response = apply_personality(f"Ohayou gozaimasu, {user.first_name}-senpai! Como posso servi-lo hoje?", "happy")
    await update.message.reply_text(response)
    await send_reaction(update, "happy")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text
    
    # Simular digitação
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    time.sleep(random.uniform(0.5, 1.5))
    
    # Obter resposta do Dialogflow
    dialogflow_response = get_dialogflow_response(
        user_id=user.id,
        text=text,
        project_id=DIALOGFLOW_PROJECT_ID
    )
    
    # Aplicar personalidade
    final_response = apply_personality(dialogflow_response)
    
    # Salvar conversa
    save_conversation(user.id, text, final_response, "default")
    
    # Enviar resposta
    await update.message.reply_text(final_response)
    
    # Ações aleatórias
    if random.random() < 0.3:
        emotion = detect_emotion(text)
        await send_reaction(update, emotion)
    if random.random() < 0.2:
        await send_waifu_image(update, "happy")

def apply_personality(text, emotion="default"):
    """Adiciona elementos kawaii à resposta"""
    traits = PERSONALITY["speech_patterns"]
    prefix = random.choice(traits["prefixes"])
    suffix = random.choice(traits["suffixes"])
    return prefix + text + suffix

async def send_reaction(update: Update, emotion: str):
    """Envia uma reação emocional"""
    reactions = PERSONALITY["speech_patterns"]["reactions"].get(emotion, ["*sorri*"])
    reaction = random.choice(reactions)
    await update.message.reply_text(reaction)

async def send_waifu_image(update: Update, emotion: str):
    """Gera e envia imagem da waifu"""
    img_bytes = generate_waifu_image(emotion)
    await update.message.reply_photo(photo=InputFile(img_bytes, filename="kaoruko.jpg"))

async def send_voice_message(update: Update, text: str):
    """Envia mensagem de voz"""
    voice = generate_waifu_voice(text, "ja")
    await update.message.reply_voice(voice=InputFile(voice, filename="kaoruko_voice.mp3"))

def detect_emotion(text):
    """Detecta emoção baseada no texto"""
    text = text.lower()
    if any(word in text for word in ["amo", "gosto", "adoro", "love"]):
        return "love"
    elif any(word in text for word in ["triste", "chateado", "chateada", "sad"]):
        return "sad"
    elif any(word in text for word in ["vergonha", "tímido", "tímida"]):
        return "shy"
    return "happy"

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Iniciar o bot
    app.run_polling()

if __name__ == "__main__":
    main()
