import os

from dotenv import load_dotenv

load_dotenv(".env")

API_ID: int = os.getenv('API_ID', 23422180)
API_HASH: str = os.getenv('API_HASH', "601d3571a55cea15453c0afcda0978a6")

BOT_TOKEN = os.getenv("7288216744:AAGpB-EReivQY4FooHFrtpYfRhij9fQ3ZDQ")

OWNER_ID = int(os.getenv("5360878379"))

LOGS_MAKER_UBOT = int(os.getenv("https://files.catbox.moe/7bz9vu.jpg"))

MAX_BOT = int(os.getenv("MAX_BOT"))

RMBG_API = os.getenv("RMBG_API")

OPENAI_KEY = os.getenv("OPENAI_KEY")

MONGO_URL = os.getenv("MONGO_URL")
