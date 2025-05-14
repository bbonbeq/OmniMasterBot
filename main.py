import discord
from discord.ext import commands
import config

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

# Load extensions
startup_extensions = ['cogs.utility', 'cogs.moderation', 'music.music']
for ext in startup_extensions:
    bot.load_extension(ext)

@bot.event
async def on_ready():
    print(f"✅ OmniMaster is online as: {bot.user}")
    await bot.change_presence(activity=discord.Game(name=f'Type {config.PREFIX}help'))

bot.run(config.TOKEN)

