import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Configurações do Google Cloud
DIALOGFLOW_PROJECT_ID = os.getenv("DIALOGFLOW_PROJECT_ID")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Configurações da Kaoruko
KAORUKO_NAME = "Kaoruko-chan"
DEFAULT_LANGUAGE = "pt"
