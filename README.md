# OmniMasterBot

OmniMasterBot is a powerful all-in-one Discord bot made with Python. It provides a variety of useful commands, including moderation tools, music playback, and utility commands.

## Features
- `>ping` — Responds with "Pong!" and the bot's latency.
- `>say <message>` — Repeats the message you provide.
- `>clear <amount>` — Clears a specific number of messages (Admin only).
- `>ban @user` — Bans a user from the server (Admin only).
- `>kick @user` — Kicks a user from the server (Admin only).
- `>play <url>` — Plays audio from YouTube in a voice channel.
- `>pause` — Pauses the current song.
- `>resume` — Resumes the current song.
- `>skip` — Skips the current song.
- `>join` — Makes the bot join the voice channel.
- `>leave` — Makes the bot leave the voice channel.

## Setup

To get the bot up and running, follow these steps:

### 1. Create a Virtual Environment (Recommended)
It's always a good idea to use a virtual environment for Python projects to manage dependencies.

```bash
# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

