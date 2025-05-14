from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'🧹 Cleared {amount} messages.', delete_after=3)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'👢 {member.mention} has been kicked.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'🚫 {member.mention} has been banned.')

def setup(bot):
    bot.add_cog(Moderation(bot))

