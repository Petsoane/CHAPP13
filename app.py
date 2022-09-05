"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from DadJokes import dadjokes
import random

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    msg = """
    Hi! This is a dad joke bot that echos back every message sent to it
    except the message 'hello'
    I more features will be added as I learn how eacch api works.
    I still need to find the best api for for the job as well.
    """

    update.message.reply_text(msg)


def help(update, context):
    """Send a message when the command /help is issued."""
    msg = """
    Hi! This is a dad joke bot that echos back every message sent to it
    except the message 'hello'
    I more features will be added as I learn how eacch api works.
    I still need to find the best api for for the job as well.
    """


    update.message.reply_text(msg)


def echo(update, context):

    """
    Echo the user message, or Send a dadjoke when the message is
    'hello'
    """
    if (update.message.text == "hello"):
        update.message.reply_text(random.choice(dadjokes))
    else:
        update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5750214131:AAE_lVnxeI690D4qweeUNHShgXMCTY4-Fxc", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    # updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=3978,
                          url_path="5750214131:AAE_lVnxeI690D4qweeUNHShgXMCTY4-Fxc")
    updater.bot.setWebhook('https://chapp13bot.herokuapp.com/5750214131:AAE_lVnxeI690D4qweeUNHShgXMCTY4-Fxc')

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
