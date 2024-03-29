import discord
import asyncio
import requests
from discord.ext import commands


class Covid(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def covid(self, ctx, *, countryName=None):
        try:
            if countryName is None:
                embed = discord.Embed(title="This command is used like this: ```#covid [country]```", colour=0xff0000,
                                      timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)


            else:
                url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                todayCases = json_stats["todayCases"]
                totalDeaths = json_stats["deaths"]
                todayDeaths = json_stats["todayDeaths"]
                recovered = json_stats["recovered"]
                active = json_stats["active"]
                critical = json_stats["critical"]
                casesPerOneMillion = json_stats["casesPerOneMillion"]
                deathsPerOneMillion = json_stats["deathsPerOneMillion"]
                totalTests = json_stats["totalTests"]
                testsPerOneMillion = json_stats["testsPerOneMillion"]

                embed2 = discord.Embed(title=f"**COVID-19 Status Of {country}**!",
                                       description="This Information Was Brought To You By #CAB!",
                                       colour=0xA30000, timestamp=ctx.message.created_at)
                embed2.add_field(name="**Total Cases**", value=totalCases, inline=True)
                embed2.add_field(name="**Today Cases**", value=todayCases, inline=True)
                embed2.add_field(name="**Total Deaths**", value=totalDeaths, inline=True)
                embed2.add_field(name="**Today Deaths**", value=todayDeaths, inline=True)
                embed2.add_field(name="**Recovered**", value=recovered, inline=True)
                embed2.add_field(name="**Active**", value=active, inline=True)
                embed2.add_field(name="**Critical**", value=critical, inline=True)
                embed2.add_field(name="**Cases Per One Million**", value=casesPerOneMillion, inline=True)
                embed2.add_field(name="**Deaths Per One Million**", value=deathsPerOneMillion, inline=True)
                embed2.add_field(name="**Total Tests**", value=totalTests, inline=True)
                embed2.add_field(name="**Tests Per One Million**", value=testsPerOneMillion, inline=True)

                embed2.set_thumbnail(
                    url="https://media.discordapp.net/attachments/402845526791290881/837450301501210654/E0Kt7iFVoAIdV6T.png?width=714&height=676")
                await ctx.send(embed=embed2)

        except:
            embed3 = discord.Embed(title="Invalid Country Name Or API Error! Try Again..!", colour=0xff0000,
                                   timestamp=ctx.message.created_at)
            embed3.set_author(name="Error!")
            await ctx.send(embed=embed3)


def setup(client):
    client.add_cog(Covid(client))
