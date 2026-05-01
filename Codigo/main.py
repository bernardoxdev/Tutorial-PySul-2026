from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

from handlers import start, echo, api

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# registrar handlers
start.register(app)
echo.register(app)
api.register(app)

if __name__ == "__main__":
    print("Bot iniciado...")
    app.run()