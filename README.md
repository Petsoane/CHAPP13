# CHAPP13
A simple telegram chatbot the responds to with dad jokes

# Installing

simply clone this repo then run 

_source ./CHAPPIE/bin/activate_
_python -m pip install -r requirements.txt_
_python app.py_

# Requirements and outline

This is a simple technical challenge to demonstrate my ability to learn on fly while being resourcesful.

Build a _simple_ chatbot that does the followint: 
    - Receive a "Hello" from anyone on telegram
    - THe bot then replies with a dad joke.


# Breakdown

## Chatbot part.

This is going to use the *python-telegram-bot* package. This is a wrapper around
telegrams api. Still reading on all the available functionalities.

## dad jokes

For simplicity I am simply creating a list of dad jokes that are then converted into a list.
This list is used to randomly choose a joke and sends it back to telegram.

The reason for doing it this way is because ~PTB~ seems to crash when I used 
other packages that access the internet for generating dad jokes. 
I still need to work on it.



    
