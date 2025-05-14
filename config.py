import os
from dotenv import load_dotenv

# Ładowanie zmiennych środowiskowych z pliku .env
load_dotenv()

# Discord Bot Token
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Bot Command Prefix
PREFIX = '>'

# Opcjonalne zmienne konfiguracyjne:
# ID serwera, w którym bot ma działać (możesz ustawić, jeśli bot działa tylko w jednym serwerze).
GUILD_ID = os.getenv('GUILD_ID', 'default_guild_id_here')

# Channel ID dla kanału powitalnego (opcjonalnie).
WELCOME_CHANNEL_ID = os.getenv('WELCOME_CHANNEL_ID', 'default_channel_id_here')

# ID roli administratora (jeśli masz rolę administracyjną do ograniczonych komend).
ADMIN_ROLE_ID = os.getenv('ADMIN_ROLE_ID', 'default_admin_role_id_here')
