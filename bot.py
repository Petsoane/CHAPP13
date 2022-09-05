import logging
import telegrampy
from telegrampy.ext import commands


logging.basicConfig(level=logging.INFO, format="(%(asctime)s) %(levelname)s %(message)s", datefmt="%m/%d/%y - %H:%M:%S %Z")
logger = logging.getLogger("telegrampy")

bot = commands.Bot("5750214131:AAE_lVnxeI690D4qweeUNHShgXMCTY4-Fxc")

@bot.command()
async def hi(ctx):
    await ctx.send("Hello")

bot.run()
