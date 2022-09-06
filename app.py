"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
This is a dadjoke echo bot.
It echoes back any message sent it except the hello message.

TODO add ability to to toggle the echo behavoir
"""

import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from DadJokes import dadjokes
import random

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

global echomode
echomode = False

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    msg = """
    Hi! This is a dad joke bot that echos back every message sent to it\
    except the message 'hello'\
    I more features will be added as I learn how eacch api works.\
    I still need to find the best api for for the job as well.\
    """

    update.message.reply_text(msg)


def help(update, context):
    """Send a message when the command /help is issued."""
    msg = """
    Hi! This is a dad joke bot that echos back every message sent to it\
    except the message 'hello'
    I more features will be added as I learn how eacch api works.
    I still need to find the best api for for the job as well.
    """
    update.message.reply_text(msg)

def echo_toggle(update, context):
    global echomode
    echomode = not echomode
    update.message.reply_text("echomode enabled")


def echo(update, context):
    """
    Echo the user message, or Send a dadjoke when the message is
    'hello'
    """
    logger.info("Got new messsage: %s", update.message.text)
    if (update.message.text == "hello"):
        update.message.reply_text(random.choice(dadjokes))
    elif echomode:
        logger.info("echomode toggled: %s", str(echomode))
        update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5586672700:AAHJQSejb52P5zHttrURKYRzh9UwmhyVra8", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("echo", echo_toggle))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # TODO Figure out how to setup the bot with webhooks on herokuu.
    # updater.start_webhook(listen="127.0.0.1",
    #                       port=PORT,
    #                       url_path='5586672700:AAHJQSejb52P5zHttrURKYRzh9UwmhyVra8')
    # # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    # updater.bot.set_webhook('https://afternoon-journey-78467.herokuapp.com/5586672700:AAHJQSejb52P5zHttrURKYRzh9UwmhyVra8')
    # # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    # TODO test if this idle affects the program at all.
    # updater.idle()


if __name__ == '__main__':
    main()
