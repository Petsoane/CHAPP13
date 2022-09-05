#!/usr/bin/env python3
from TelegramBot8 import Message, TeleBot, Update, ParseMode

API_KEY = "5750214131:AAE_lVnxeI690D4qweeUNHShgXMCTY4-Fxc"
bot = TeleBot(API_KEY)

@bot.add_command_helper(command="/hi")
def hi(message: Message):
    bot.send_message(message.chat.getID(), "Hello")


@bot.add_command_menu_helper(command="/bye", description="Just testing added command")
def bye(message: Message):
    bot.send_message(message.chat.getID(), "Bye")


@bot.add_regex_helper(regex="^hi$")
def regex(message: Message):
    bot.send_message(message.chat.getID(), "Hello")

bot.poll()
