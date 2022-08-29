import disnake, os
from disnake.ext import commands
from dotenv import load_dotenv
load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}.")


try: 
    bot.run(TOKEN)

except Exception as error:
    print(f'Failed to start. \n\nInfo: {error}')