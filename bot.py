# bot.py
# Helpful links: https://discordpy.readthedocs.io/en/stable/api.html#messages
# Install dicord-py-slash-command # pip install -U discord-py-slash-command
import os
import os.path
import sys
import discord
import asyncio  # Timer
from dotenv import load_dotenv
from discord.ext import tasks
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import CommandNotFound # Get rid of 'discord.ext.commands.errors.CommandNotFound:' error

load_dotenv() # read the .env file
description = '''
God, this is annoying as all hell.
Fuck Python in it's stupid magical ass.
'''

TOKEN = os.getenv('DISCORD_TOKEN')  # BOT Token
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(description=description, command_prefix="?", intents=intents) # Bot listens to ? as command

# Start the bot, and print in CLI window
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
 #   print(f"Invite link: https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8") # To invite the bot
    print('------')
    try:
        synced = await bot.tree.sync()
    except Execption as e:
        print(e)
# END

# Events -- Things that happen
@bot.event
async def on_message(message: discord.Message):
    if message.author.bot: # Let's not respond to ourselves.
         return
#

## Bot Commands
@bot.command(name="ping",
             help="Test the bots responsiveness.",
             brief="Is the bot alive? ... am I alive?")
async def ping_pong(ctx):
	await ctx.channel.send(f"Pong! Bot Ping is: ({bot.latency*1000}ms)")
##

## Slash Commands
@bot.tree.command(name="ping")  # Define a guild command.
async def _ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! ({bot.latency*1000}ms)")

# Reply to sender
@bot.tree.command(name="hello", description="Say Hello!")
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hi there!", ephemeral=True)
##

# NO NEED TO EDIT PAST THIS LINE
# Remove 'discord.ext.commands.errors.CommandNotFound: Command' from terminal window. 
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):  # Using `==` is incorrect
        return
    raise error

bot.run(TOKEN)
