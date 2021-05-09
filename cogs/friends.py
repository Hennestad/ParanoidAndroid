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

            elif str(message.author) == "B E P I S#2925":
                await message.channel.send('Nom!')

            elif str(message.author) == "Looland#8359":
                await message.channel.send('Amogus')
                await message.channel.send("https://i1.sndcdn.com/artworks-TOJJyHynzM0iRSuW-9URBDA-t500x500.jpg")

            elif str(message.author) == "adispinjic#6655":
                await message.channel.send('Adis! Har du sett Fredrik??')

            elif str(message.author) == "Rylance#6969":
                await message.channel.send('Lewis! Have you seen Fredrik?? Please find him, he owes me money!')

            elif str(message.author) == "akvanvig#4328":
                await message.channel.send('Hei Anders! Visste du dette?: Mao Zedong (tradisjonell kinesisk: 毛澤東, '
                                           'forenklet kinesisk: 毛泽东, pinyin: Máo Zédōng; Wade-Giles: Mao Tse-tung, '
                                           'født 26. desember 1893 i Shaoshan i Hunan i Kina, død 9. september 1976 i '
                                           'Beijing) var en kinesisk kommunist, statsleder, revolusjonær og '
                                           'teoretiker. Han ledet Kinas kommunistparti til seier i den kinesiske '
                                           'borgerkrigen og grunnla Folkerepublikken Kina i 1949, som han ledet fram '
                                           'til sin død i 1976. Mao er også grunnleggeren av en retning innen '
                                           'marxismen-leninismen kjent som maoismen.')
                await message.channel.send("https://media.snl.no/media/67119/standard_compressed_sz8318b2.jpg")

            else:
                await message.channel.send('Hei! Har du sett Fredrik? Kan du be han si hei til meg?')


def setup(client):
    client.add_cog(Friends(client))
