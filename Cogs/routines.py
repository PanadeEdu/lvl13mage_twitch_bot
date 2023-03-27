from twitchio.ext import commands, routines

class Routines(commands.Cog):
    def __init__(self, bot: commands.Bot, users):
        self.bot = bot
        self.users = users

    @routines.routine(minutes=3)
    async def notifier(self):
        try:
            await self.bot.connected_channels[0].send(f'Ich habe einen besonderen Bot am laufen. Checkt ihn mal aus: https://commands.lvl13mage.live')
        except:
            print("Error while sending message to twitch chat.")
    notifier.start()

    @routines.routine(seconds=30)
    async def persist(self):
        # This will be called every 5 minutes
        print('Persisting users...')
        self.users.persist_users('users.txt')
        print('Done.')
    persist.start()