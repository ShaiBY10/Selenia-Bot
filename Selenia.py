from discord.ext import commands, tasks
import os
from random import choice
from helpcog import HelpCog
from musiccog import MusicCog
from badWords import bad_words
from zoz import link_generator
from zoz import link

bot = commands.Bot(command_prefix="!")
bot.remove_command('help')
bot.add_cog(HelpCog(bot))
bot.add_cog(MusicCog(bot))


# # --Bad Words catcher-- #
# @bot.event
# async def on_message(msg):
# 	for word in bad_words:
# 		if word in msg.content:
# 			await msg.channel.send(f'{msg.author.mention} Dont say that! \n Your words can hurt! \n Think twice before saying them!')
# 			await msg.channel.edit('Im a selfish guy who thinks only about himself.')


# --COMMAND-- # says what the user puts in ""
@bot.command(name='say', help='Repeat what you write(use "and write your text here". ')
async def say(ctx, arg):
    await ctx.send(arg)


# --COMMAND-- # send a message
@bot.command(name='king', help='information about who is the king.')
async def king(ctx):
    await ctx.send('Well the king is definitely **ShaiBY** since he created ME :D')


# --COMMAND-- # send a message
@bot.command(name='noob', help='Information about who is noob.(He is really noob and he is also a dick!')
async def noob(ctx):
    await ctx.send(
        'The noob of this server is clearly Gabi Gab Gab Shemesh since he tries all these failed flip reset\'s and he is just STINKY NOOB!')


# --COMMAND-- # send a message
@bot.command(name='actualking', help='Information about who is the actual king.')
async def actualking(ctx):
    await ctx.send('The Real king of this server and this world is Lord (Zoz Suli) Morad. ')


# --COMMAND-- # send a zoz
@bot.command(name='zoz', help="Receive random picture of Zozikim")
async def zoz(ctx):
    await ctx.send(link_generator(str(link)))


TOKEN = os.environ.get('BOT_TOKEN')
bot.run(TOKEN)
