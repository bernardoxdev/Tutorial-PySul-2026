from pyrogram import filters
from services.api_service import get_crypto_price

def register(app):
    @app.on_message(filters.command("crypto"))
    def crypto(client, message):
        price = get_crypto_price()

        if price:
            message.reply(f"💰 Bitcoin: ${price}")
        else:
            message.reply("⚠️ Erro ao buscar preço.")