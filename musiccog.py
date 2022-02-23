import discord
from discord.ext import commands
from youtube_dl import YoutubeDL


class MusicCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

		# all the music related stuff
		self.is_playing = False
		self.is_paused = False

		# 2d array containing [song, channel]
		self.music_queue = []
		self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'False'}
		self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

		self.vc = None

	# searching the item on YouTube
	def search_yt(self, item):
		with YoutubeDL(self.YDL_OPTIONS) as ydl:
			try:
				info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
			except Exception:
				return False

		return {'source': info['formats'][0]['url'], 'title': info['title']}

	def play_next(self):
		if len(self.music_queue) > 0:
			self.is_playing = True

			# get the first url
			m_url = self.music_queue[0][0]['source']

			# remove the first element as you are currently playing it
			self.music_queue.pop(0)

			self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
		else:
			self.is_playing = False

	# infinite loop checking
	async def play_music(self, ctx):
		if len(self.music_queue) > 0:
			self.is_playing = True

			m_url = self.music_queue[0][0]['source']

			# try to connect to a voice channel if you are not already connected
			if self.vc == None or not self.vc.is_connected():
				self.vc = await self.music_queue[0][1].connect()

				# in case we fail to connect
				if self.vc == None:
					await ctx.send("Could not connect to the voice channel")
					return
			else:
				await self.vc.move_to(self.music_queue[0][1])

			# remove the first element as you are currently playing it
			self.music_queue.pop(0)

			self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
		else:
			self.is_playing = False

	@commands.command(name="play", help="Play music command")
	async def play(self, ctx, *args):
		query = " ".join(args)

		voice_channel = ctx.author.voice.channel
		if voice_channel is None:
			await ctx.send("You are not connected to a voice channel, \n Enter a voice channel to continue!")
		elif self.is_paused:
			self.vc.resume()
		else:
			song = self.search_yt(query)
			if type(song) == type(True):
				await ctx.send("Could not download the song. Try a different search please!")
			elif self.is_playing == True:
				await ctx.send("Added song to playlist")
			else:
				await ctx.send(f" I Started playing **{song['title']}** in {voice_channel} channel, Come listen :D ")
				self.music_queue.append([song, voice_channel])

				if self.is_playing == False:
					await self.play_music(ctx)

	@commands.command(name="pause", help="Pause the current song")
	async def pause(self, ctx, *args):
		if self.is_playing:
			self.is_playing = False
			self.is_paused = True
			self.vc.pause()
		elif self.is_paused:
			self.is_playing = True
			self.is_paused = False
			self.vc.resume()

	@commands.command(name="resume", aliases=["r"], help='Resumes playing the current song')
	async def resume(self, ctx, *args):
		if self.is_paused:
			self.is_playing = True
			self.is_paused = False
			self.vc.resume()

	@commands.command(name="skip", aliases=["s", "next"], help="Skips the current song")
	async def skip(self, ctx):
		variable = ""

		for i in range(0, len(self.music_queue)):
			if i > 4: break
			variable += self.music_queue[i][0]['title'] + '\n'

		if variable != "":
			await ctx.send(variable)
		else:
			await ctx.send("No music in queue, nothing to skip to...")

	@commands.command(name="leave", aliases=["disconnect", "l", "d"], help="Leaves the voice channel im currently in.")
	async def leave(self, ctx):
		self.is_playing = False
		self.is_paused = False
		await ctx.send("Cya around! :)")
		await self.vc.disconnect()
