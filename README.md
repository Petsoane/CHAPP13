# CHAPP13
A simple telegram chatbot the responds to with dad jokes

# Requirements and outline

This is a simple technical challenge to demonstrate my ability to learn on fly while being resourcesful.

Build a _simple_ chatbot that does the followint: 
    - Receive a "Hello" from anyone on telegram
    - THe bot then replies with a dad joke.


# Breakdown

## Chatbot part.

Given that this is going to be a telegram chatbot, all I need to figure out
is how am I going to interact with the API. 

Searching for compatible packages in _pypi_ lead me to a couple possible
api frameworks and packages such as **telegrampy** and *python-telegram-bot* and
*botup*.

I ended using Telebot since it has the least configration hassle after installation and the syntax seems to be keeping in more with pythons own philosophies, rather than 
trying to keep to Telegrams design and structure. 
This abstraction makes even faster to develop custom chatbots without have to deal
with Telegrams boiler plate.

This part of the bot is kep simple for now, using stock example code. I am going to add
some customs responses as well _chatbot-utils_. I find this module simplifies 
chatbot context/response mapping.

## dad jokes

Joking is a python package that automatically fetches jokes from the internet.

I really like that it can also get multiple other kinds of jokes meaning I can use telegrams bot commads functionality to add other jokes to the bot as
time moves forward




    
