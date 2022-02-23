from discord.ext import commands, tasks
import os
from random import choice
from helpcog import HelpCog
from musiccog import MusicCog


bot = commands.Bot(command_prefix="!")
bot.remove_command('help')
bot.add_cog(HelpCog(bot))
bot.add_cog(MusicCog(bot))

# status change
status = ['Shai is AWSOME!', 'Some music', 'Gabgab is nerd!']



TOKEN = os.environ.get('BOT_TOKEN')
bot.run('TOKEN')
