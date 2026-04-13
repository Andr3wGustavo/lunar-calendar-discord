import discord
from discord.ext import commands
import os
import logging
from dotenv import load_dotenv
import asyncio
from utils.db import init_db

# Configure advanced logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(name)s | %(message)s')
logger = logging.getLogger("LunarBot")

load_dotenv()

class LunarBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.default(),
            help_command=None
        )

    async def setup_hook(self):
        await init_db()
        await self.load_extension('cogs.lunar')
        await self.tree.sync()
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")
        logger.info("Bot is ready and aligned with the Maya 3D plane.")

bot = LunarBot()

if __name__ == '__main__':
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        logger.error("Please set DISCORD_TOKEN in .env file")
    else:
        bot.run(TOKEN)
