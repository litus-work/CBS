from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env", override=False)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENWEATHER_TOKEN = os.getenv("OPENWEATHER_TOKEN")

if not TELEGRAM_TOKEN:
    raise RuntimeError("Не знайдено TELEGRAM_TOKEN у .env або змінних середовища")
if not OPENWEATHER_TOKEN:
    raise RuntimeError("Не знайдено OPENWEATHER_TOKEN у .env або змінних середовища")