import discord
from discord.ext import commands
from asyncio import sleep as s


class Grandis(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remind(self, ctx, time: int, msg):
        embed = discord.Embed(title='Reminder set',
                              description=f"{ctx.author.mention}, I have set a reminder for {msg} in {time} minutes!",
                              colour=discord.Colour.blurple())
        embed.timestamp = ctx.message.created_at
        await ctx.send(embed=embed)
        await s(60*time)
        await ctx.send(f'{msg} {ctx.author.mention}')


def setup(client):
    client.add_cog(Grandis(client))
