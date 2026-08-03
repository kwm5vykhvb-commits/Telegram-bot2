import os
from telethon import TelegramClient, events

API_ID = 123456 
API_HASH = 'ton_api_hash'
BOT_TOKEN = os.getenv('BOT_TOKEN')

client = TelegramClient('bot2_session', API_ID, API_HASH)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('🔥 Salut ! Je suis le Bot2. Je tourne H24 sur Render')

@client.on(events.NewMessage(pattern='/ping'))
async def ping(event):
    await event.reply('Pong ✅')

print("Bot2 démarré...")
client.start(bot_token=BOT_TOKEN)
client.run_until_disconnected()
