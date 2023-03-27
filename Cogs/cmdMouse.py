from Utility.mouseMacro import MouseMacro
from twitchio.ext import commands

class CmdMouse(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def mrandom(self, ctx):
        MouseMacro.mouse_random()

    @commands.command()
    async def mup(self, ctx):
        MouseMacro.mouse_up()

    @commands.command()
    async def mdown(self, ctx):
        MouseMacro.mouse_down()

    @commands.command()
    async def mleft(self, ctx):
        MouseMacro.mouse_left()

    @commands.command()
    async def mright(self, ctx):
        MouseMacro.mouse_right()

    def getHelp():
        # return a multiline string with all commands and their description formated as list
        return f'Maus Commands:\
                ?mrandom - Bewegt die Maus auf eine zufällige Position.\
                ?mup - Bewegt die Maus nach oben.\
                ?mdown - Bewegt die Maus nach unten.\
                ?mleft - Bewegt die Maus nach links.\
                ?mright - Bewegt die Maus nach rechts.'