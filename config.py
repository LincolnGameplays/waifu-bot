# ~/waifu-bot/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do arquivo .env

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Token seguro
WAIFU_NAME = "Kaoruko-chan"
DEFAULT_LANGUAGE = "pt"
