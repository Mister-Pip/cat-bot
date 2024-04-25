import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("TG_API")
RAND_FACT_API = os.getenv("RAND_FACT_API")