from Utility.keyboardMacro import KeyboardMacro
from twitchio.ext import commands

class CmdKeyboard(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def jump(self, ctx):
        KeyboardMacro.press_jump()

    def getHelp():
        # return a multiline string with all commands and their description formated as list
        return f'Tastatur Commands:\
                ?jump - Drückt die Leertaste.'