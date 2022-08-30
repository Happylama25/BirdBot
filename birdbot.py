import disnake, os
from Blink import *
from Buzz import *
import RPi.GPIO as GPIO
import time
from disnake.ext import commands
from dotenv import load_dotenv
load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=disnake.Intents.all(), reload=True)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}.")


@bot.command(aliases=[""])
async def hello(ctx):
    await ctx.send('birb')

@bot.command()
async def blink(ctx):
    await ctx.send('Blinking red LED 5 times')
    async with ctx.typing():
        setup()
        loop()
    await ctx.send('Finished')

@bot.command()
async def buzz(ctx):
    await ctx.send('Buzzing 5 times')
    async with ctx.typing():
        setupbuzz()
        loopbuzz()
    await ctx.send('Finished')



try: 
    bot.run(TOKEN)

except Exception as error:
    print(f'Failed to start. \n\nInfo: {error}')