from telethon import TelegramClient, events
import asyncio
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration variables from environment variables
api_id = os.getenv('API_ID')  # Ensure you have these in your .env file
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')

# Initialize the Telegram Client
client = TelegramClient('session_name', api_id, api_hash)

async def list_chats():
    async for dialog in client.iter_dialogs():
        print(f"{dialog.name} has ID {dialog.id}")

async def main():
    await client.start(phone=lambda: phone)
    await list_chats()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
