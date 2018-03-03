import discord
from discord.ext import commands

class Punch:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Punch(self):
        “””Punch a user!”””

        #Your code will go here
        await self.bot.say('ONE PUNCH! And ' + user.mention + ' is out! ლ(ಠ益ಠლ)')

def setup(bot):
    bot.add_cog(Punch(bot))
