import discord
from discord.ext import commands
from discord.ext.commands import bot


class help_cog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

		self.help_message = """
		General commands:
		!help - displays all the available commands
		!play <keyword> plays a song in your the current channel
		!queue - displays the current music queue
		!skip - skips the current song being played
		!leave - kicks the bot from the voice channel
		!pause - pauses the current song playing or resumes if already pasued
		!resume = resumes playing the current song
		"""

		self.text_channel_text = []

	@commands.Cog.listener()
	async def on_ready(self):
		for guild in self.bot.guilds:
			for channel in guild.text_channels:
				self.text_channel_text.append(channel)

				await self.send_to_all("Hello guys im online :D")
				print(f"Connected sucssesfully")

	async def send_to_all(self, msg):
		for text_channel in self.text_channel_text:
			await text_channel.send(msg)

	@commands.command(name='help', help='displays all the available commands')
	async def help(self, ctx):
		await ctx.send(self.help_message)
