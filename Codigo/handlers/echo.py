from pyrogram import filters
from utils.state import set_state, get_state, clear_state

def register(app):
    @app.on_message(filters.command("echo"))
    def echo_start(client, message):
        set_state(message.from_user.id, "echo")
        message.reply("Digite algo que eu repito:")

    @app.on_message(filters.text)
    def echo_response(client, message):
        user_id = message.from_user.id

        if get_state(user_id) == "echo":
            message.reply(f"🔁 {message.text}")
            clear_state(user_id)