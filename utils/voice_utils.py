from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup
from io import BytesIO

def generate_waifu_voice(text, lang="ja", emotion="default"):
    # Gerar voz base
    tts = gTTS(text=text, lang=lang, slow=False)
    voice_io = BytesIO()
    tts.write_to_fp(voice_io)
    voice_io.seek(0)
    
    # Converter para AudioSegment
    audio = AudioSegment.from_file(voice_io, format="mp3")
    
    # Aplicar efeitos de voz de anime
    audio = speedup(audio, playback_speed=1.3)  # Voz mais rápida
    
    if emotion == "happy":
        audio = audio + 5  # Aumentar volume
    elif emotion == "sad":
        audio = audio - 100  # Baixar tom
    
    # Exportar para buffer
    output = BytesIO()
    audio.export(output, format="mp3")
    output.seek(0)
    
    return output
