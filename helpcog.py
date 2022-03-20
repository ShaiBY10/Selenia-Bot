import discord
from discord.ext import commands, tasks
from discord.ext.commands import bot
from random import choice


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.text_channel_text = []

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)

                # await self.send_to_all("Hello guys im online :D")
                print(f"Connected successfully as {self.bot.user}")

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_text:
            await text_channel.send(msg)


# status change
status = ['Shai is AWSOME!', 'Some music', 'Gabgab is nerd!']
