from discord.ext import commands
import discord
import youtube_dl
import asyncio

ytdl = youtube_dl.YoutubeDL({'format': 'bestaudio', 'noplaylist': True})
ffmpeg_options = {'options': '-vn'}

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = asyncio.Queue()
        self.play_next = asyncio.Event()
        self.current = None

    async def player_loop(self, ctx):
        while True:
            self.play_next.clear()
            url = await self.queue.get()
            info = ytdl.extract_info(url, download=False)
            source = await discord.FFmpegOpusAudio.from_probe(info['url'], **ffmpeg_options)
            ctx.voice_client.play(source, after=lambda e: self.play_next.set())
            await ctx.send(f'▶️ Now playing: **{info["title"]}**')
            await self.play_next.wait()

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
        else:
            await ctx.send('❌ You are not in a voice channel.')

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send('❌ I am not in a voice channel.')

    @commands.command()
    async def play(self, ctx, url: str):
        if not ctx.voice_client:
            await ctx.invoke(self.join)
        await self.queue.put(url)
        if not self.current:
            self.current = self.bot.loop.create_task(self.player_loop(ctx))

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send('⏸️ Paused.')

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send('▶️ Resumed.')

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send('⏭️ Skipped.')

def setup(bot):
    bot.add_cog(Music(bot))

