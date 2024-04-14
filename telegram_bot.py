from telethon import TelegramClient, events
import requests
import json
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
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')
discord_webhook_url_1 = os.getenv('DISCORD_WEBHOOK_URL')
chat_id_1 = int(os.getenv('CHAT_ID'))  # Ensure it's converted to int if needed

# Initialize the Telegram Client
client = TelegramClient('session_name', api_id, api_hash)

async def forward_message_to_discord(message, discord_webhook_url):
    message_content = message.text or message.caption
    if message_content:
        discord_data = {
            "embeds": [
                {
                    "title": "New Message From Telegram",
                    "description": message_content,
                    "color": 5814783
                }
            ]
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(discord_webhook_url, data=json.dumps(discord_data), headers=headers)
        if response.status_code in [200, 204]:
            logger.info("Message forwarded to Discord successfully.")
        else:
            logger.error(f"Failed to forward message to Discord: {response.status_code}, {response.text}")
    else:
        logger.info("No text found in the message after delay.")

@client.on(events.NewMessage(chats=[chat_id_1]))  # Use the chat_id_1 variable
async def handle_new_message(event):
    await asyncio.sleep(2)  # Wait for possible edits
    message = await client.get_messages(event.chat_id, ids=event.message.id)
    if event.chat_id == chat_id_1:  # Confirming the chat ID
        await forward_message_to_discord(message, discord_webhook_url_1)

async def main():
    logger.info("Bot is starting...")
    await client.start(phone=lambda: phone)
    logger.info("Bot is now running and listening for new messages...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
