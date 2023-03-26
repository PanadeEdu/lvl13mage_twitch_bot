from twitchio.ext import commands
from Utility.mechabellumMacro import MechabellumMacro
from pprint import pprint

class CmdMechabellum(commands.Cog):
    
        def __init__(self, bot: commands.Bot):
            self.bot = bot
    
        @commands.command(aliases={'shield'})
        async def buyshield(self, ctx):
            MechabellumMacro.buy_shield()

        @commands.command(aliases={'rocket'})
        async def buyrocket(self, ctx):
            MechabellumMacro.buy_rocket()
        
        @commands.command(aliases={'unit'})
        async def buyunit(self, ctx):
            message_params = ctx.message.content.split(' ')
            MechabellumMacro.buy_unit(int(message_params[1]))

        def getHelp():
            # return a multiline string with all commands and their description formated as list
            return f'Mechabellum Commands:\
                    ?buyshield - Kaufe ein Schild.\
                    ?buyrocket - Kaufe eine Rakete.\
                    ?buyunit <slot number> - Kaufe einheit auf dem gewählten slot. (rechtsoben nach linksunten)'