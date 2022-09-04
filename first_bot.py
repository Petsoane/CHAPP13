import logging
from telebot import TeleBot
from dadjokes import Dadjoke

app = TeleBot(__name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


@app.route('/command ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Command Recieved: {}".format(cmd)

    logging.info(f"structure the message object {message}")


    app.send_message(chat_dest, msg)


@app.route('/start ?(.*)')
def start_command(message, cmd):
    chat_dest = message['chat']['id']
    # msg = "Command Recieved: {}".format(cmd)
    msg = f"welcome to the dad jokes command {cmd}"

    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
   chat_dest = message['chat']['id']
   user_msg = message['text']

   if user_msg == 'hello':
       msg = Dadjoke().joke
   else:
       msg = "You did not greet me back bruh"

   app.send_message(chat_dest, msg)


if __name__ == '__main__':
    app.config['api_key'] = '5750214131:AAE_lVnxeI690D4qweeUNHShgXMCTY4-Fxc'
    app.poll(debug=True)
