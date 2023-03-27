from twitchio.ext import commands
from Cogs.cmdMouse import CmdMouse
from Cogs.cmdKeyboard import CmdKeyboard
from Cogs.cmdMechabellum import CmdMechabellum

class CmdGeneral(commands.Cog):

    def __init__(self, bot: commands.Bot, users):
        self.bot = bot
        self.users = users

    @commands.command()
    async def help(self, ctx: commands.Context):
        # splot ctx message content by space and check if the second parameter is a command
        message_params = ctx.message.content.split(' ')
        help_option = 'None'
        if len(message_params) > 1:
            help_option = message_params[1]

        await ctx.send(f'Hey {ctx.author.name}, einen besonderen Bot am laufen. Mehr Infos: https://commands.lvl13mage.live')
        #await ctx.send(f'Auf garkeinen Fall folgende Commands verwenden NotLikeThis :')
        #if help_option == 'None':
        #    # send help for all commands
        #    await ctx.send(CmdGeneral.getHelp())
        #    await ctx.send(CmdMouse.getHelp())
        #    await ctx.send(CmdKeyboard.getHelp())
        #    await ctx.send(CmdMechabellum.getHelp())
        #elif help_option == 'general':
        #    # send help for general commands
        #    await ctx.send(CmdGeneral.getHelp())
        #elif help_option == 'mouse':
        #    # send help for mouse commands
        #    await ctx.send(CmdMouse.getHelp())
        #elif help_option == 'keyboard':
        #    # send help for keyboard commands
        #    await ctx.send(CmdKeyboard.getHelp())
        #elif help_option == 'mechabellum':
        #    # send help for mechabellum commands
        #    await ctx.send(CmdMechabellum.getHelp())

    @commands.command()
    async def count(self, ctx: commands.Context):
        await ctx.send(f'Hey {ctx.author.name}, du hast {self.users.get_user_total_commands(ctx.author.name)} Commands verwendet. Ganz schön viel. :D')

    @commands.command()
    async def scoreboard(self, ctx: commands.Context):
        # use get_scoreboard with a limit of 10 and iterate over the list to send the scoreboard of top 10 users and their total command count
        scoreboard = self.users.get_scoreboard(10)
        await ctx.send(f'Hey {ctx.author.name}, hier ist das Scoreboard der Top 10 User die meinen Untergang wollen:')
        for user in scoreboard:
            await ctx.send(f'{user[0]} - {user[1]} cmd\'s')

    def getHelp():
        # return a multiline string with all commands and their description formated as list
        return f'General Commands:\
                ?help - Zeigt komplette Hilfe an.\
                ?help <gruppe> - Zeigt Hilfe für eine bestimmte Gruppe an. (general, mouse, keyboard, mechabellum)\
                ?count - Zeigt die Anzahl der Commands die du verwendet hast.\
                ?scoreboard - Zeigt das Scoreboard der Top 10 User die meinen Untergang wollen.'