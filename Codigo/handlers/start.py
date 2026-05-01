from pyrogram import filters

def register(app):
    @app.on_message(filters.command("start"))
    def start(client, message):
        message.reply(
            "👋 Olá! Eu sou um bot.\n\n"
            "Comandos disponíveis:\n"
            "/start - iniciar\n"
            "/crypto - ver preço do Bitcoin\n"
            "/echo - repetir mensagem"
        )