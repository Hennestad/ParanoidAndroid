import os
from discord.ext import commands

# Symbol used for calling commands
client = commands.Bot(command_prefix='#')


# Prints message telling the bot is running
@client.event
async def on_ready():
    print('Paranoid Android Ready.')


# Loads cog
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


# Unloads cog
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


# Loads extension if file ends with .py
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# runs bot
with open("token", "r", encoding="utf-8") as f:
    bottoken = f.read()

client.run(bottoken)
