from discord.ext import commands
import discord

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'🏓 Pong! {latency}ms')

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(message)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='🛠️ OmniMasterBot Commands', color=0x00ff00)
        embed.add_field(name='>ping', value='Check latency', inline=False)
        embed.add_field(name='>say <text>', value='Repeat your message', inline=False)
        embed.add_field(name='>clear <amount>', value='Delete messages (mod only)', inline=False)
        embed.add_field(name='>ban @user', value='Ban user (admin only)', inline=False)
        embed.add_field(name='>kick @user', value='Kick user (admin only)', inline=False)
        embed.add_field(name='>play <url>', value='Play music from YouTube', inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utility(bot))

