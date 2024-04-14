# Telegram_to_Discord_Forwarder

This repository contains two Python scripts that integrate Telegram with Discord. The first script forwards messages from a specified Telegram chat to a Discord channel using webhooks. The second script lists all chat IDs associated with your Telegram account, helping you to easily find the IDs needed for the message forwarder.

**Pre-requisites**

- Python 3.6 or higher
- A Telegram account
- A Discord account with permissions to manage webhooks

**Setup**
   
1.  Obtain Telegram API Credentials:
   - Go to the Telegram API authorization site: my.telegram.org
   - Log in with your Telegram phone number.
   - Click on 'API development tools' and fill out the form to create a new application.
   - Note down the 'api_id' and 'api_hash' you have been provided.

2.  Configure Discord Webhook

3.  Clone Repository and InstallDependencies
   - Download the Github repository and clone it into your Project Directory.
   - Install the following libraries using pip: ```pip install telethon aiohttp requests python-dotenv``` or run ```pip install -r requirements.txt```

4.  Set Up Enviroment Variables
   - In the .env file, replace the placeholders for 'API_ID', 'API_HASH', 'PHONE' and 'DISCORD_WEBHOOK_URL' and 'CHAT_ID'. You can create your own .env file or use the example version.

    > **Note:** This file should never be committed to version control to keep your credentials secure.


**Usage**

1. **Running the Chat ID lister**

    To list all chat IDs:

    ```python chat_ids.py```

   - This script will output the name and ID of each chat, which can be useful for setting the CHAT_ID environment variable.

2. **Running the Telegram-to-Discord Forwarder**

    To start forwarding messages:

    ```python telegram_bot.py```

   - This script listens to new messages from the specified Telegram chat and forwards them to the configured Discord channel.
   
  
**Scripts**

telegram_bot.py: Connects to Telegram, listens for new messages from a specified chat, and forwards them to Discord.

chat_ids.py: Lists all Telegram chats along with their IDs.

**Environment Variables**

| Parameter | Description |
|-----------|-------------|
| `API_ID`  | Your Telegram API ID. |
| `API_HASH`| Your Telegram API hash. |
| `PHONE`  | Your phone number associated with your Telegram account, including the country code. |
| `DISCORD_WEBHOOK_URL`| The full URL of your Discord webhook.. |
| `CHAT_ID`  | The ID of the Telegram chat from which messages will be forwarded. |

**Contributing**

Contributions are welcome! Please fork the repository and submit pull requests with any features, fixes, or improvements.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.
