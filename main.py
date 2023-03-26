from twioBot import Bot
from Utility.users import Users
from Cogs.cmdGeneral import CmdGeneral
from Cogs.cmdMouse import CmdMouse
from Cogs.cmdKeyboard import CmdKeyboard
from Cogs.cmdMechabellum import CmdMechabellum
import json
from pprint import pprint

users = Users()
users.load_users('users.txt')

config = open('config/config.json', 'r')
config = json.load(config)

print('Starting TwioBot...')
bot = Bot(config)

print('Loading CmdGeneral...')
bot.add_cog(CmdGeneral(bot, users))
print('Loading TwioMouse...')
bot.add_cog(CmdMouse(bot))
print('Loading TwioKeyboard...')
bot.add_cog(CmdKeyboard(bot))
print('Loading TwioMechabellum...')
bot.add_cog(CmdMechabellum(bot))

bot.run()

