import random

from discord.ext import commands, tasks
import os

from discord.ext.commands import MissingRequiredArgument

from helpcog import HelpCog
from musiccog import MusicCog
from zoz import img_list, imagekit
from buba import buba_list

bot = commands.Bot(command_prefix="!")
bot.add_cog(HelpCog(bot))
bot.add_cog(MusicCog(bot))


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
        'The noob of this server is clearly Gabi Gab Gab Shemesh since he tries all these failed flip reset\'s and he '
        'is just STINKY NOOB!')


# --COMMAND-- # send a message
@bot.command(name='actualking', help='Information about who is the actual king.')
async def actualking(ctx):
    await ctx.send('The Real king of this server and this world is Lord (Zoz Suli) Morad. ')


# --COMMAND-- # send a zoz
@bot.command(name='zoz', help="Receive random picture of Zozikim")
async def zoz(ctx):
    await ctx.send(random.choice(img_list))


# --COMMAND-- # send a buba
@bot.command(name='buba', help="Receive random picture of Osharit")
async def buba(ctx):
    await ctx.send(random.choice(buba_list))


@bot.command(name='uploadb', help="!uploadb <imagelink> <imgename> **The imagename can be whatever you want**")
async def uploadb(ctx, img_link, file_name):
    try:
        imagekit.upload(
            file=img_link,
            file_name=file_name,
            options={"folder": "buba"},
        )
        ctx.send(f"Image {file_name} is uploaded to buba folder successfully ")
    except MissingRequiredArgument:
        ctx.send(
            'That\'s not the format. \n Please use this format to upload a photo: \n !upload<z/b> <imagelink> '
            '<imgename> \n *The imagename can be whatever you want')


@bot.command(name='uploadz', help="!uploadz <imagelink> <imgename> **The imagename can be whatever you want**")
async def uploadz(ctx, img_link, file_name):
    try:
        imagekit.upload(
            file=img_link,
            file_name=file_name,
            options={"folder": "zoz"},
        )
        await ctx.send(f"Image {file_name} is uploaded to zoz folder successfully! ")
    except MissingRequiredArgument:
        await ctx.send(
            ' That\'s not the format. \n Please use this format to upload a photo: \n !upload<z/b> <imagelink> '
            '<imgename> \n *The imagename can be whatever you want')


TOKEN = os.environ.get('BOT_TOKEN')
bot.run(TOKEN)
