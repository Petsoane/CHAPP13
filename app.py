# app.py

from botup import Dispatcher, Sender
from botup.wsgi import WSGIApp  # using Flask

TOKEN = "token"

sender = Sender(TOKEN)
dispatcher = Dispatcher()
app = WSGIApp(__name__, botup_dispatcher=dispatcher, botup_token=TOKEN)


@dispatcher.message_handler('hello')
def hello_handler(chat_id, update):
    sender.send_message(chat_id, f'Hello {update.message.from_.first_name}')
