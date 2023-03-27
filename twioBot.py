from twitchio.ext import commands
import os

class Bot(commands.Bot):

    def __init__(self, config):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=config['twitch_access_token'], prefix='?', initial_channels=['thelvl13mage'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')