import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetching environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
SUDO_USERS = [int(user) for user in os.getenv("SUDO_USERS").split(",")]
FREE_BOT_LIMIT = int(os.getenv("FREE_BOT_LIMIT"))
