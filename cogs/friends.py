import discord
from discord.ext import commands


class Friends(commands.Cog):
    def __init__(self, user):
        self.user = user

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.user:
            return
        if message.author.bot:
            return
        if message.content.startswith("Hei!"):

            if str(message.author) == "Mr Octopus#7924":
                await message.channel.send('Hei Fredrik! Du er min bestevenn!')

            if str(message.author) == "B E P I S#2925":
                await message.channel.send('Nom!')

            if str(message.author) == "adispinjic#6655":
                await message.channel.send('Adis! Har du sett Fredrik??')

            if str(message.author) == "Rylance#6969":
                await message.channel.send('Lewis! Have you seen Fredrik?? Please find him, he owes me money!')

            else:
                await message.channel.send('Hei! Har du sett Fredrik? Kan du be han si hei til meg?')


def setup(client):
    client.add_cog(Friends(client))
