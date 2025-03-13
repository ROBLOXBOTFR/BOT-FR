import logging
import discord
from discord.ext import commands
import asyncio
import os
from utils.database import DatabaseManager

logger = logging.getLogger(__name__)

class TicketBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.guilds = True
        
        super().__init__(
            command_prefix=commands.when_mentioned_or('!'),
            intents=intents,
            help_command=None,
            activity=discord.Activity(type=discord.ActivityType.watching, name="for tickets"),
        )
        
        self.db = None
    
    async def setup_hook(self):
        logger.info("Initializing bot and loading extensions...")
        
        # Initialize database connection
        self.db = DatabaseManager()
        await self.db.init()
        
        # Load extensions (cogs)
        await self.load_extension("cogs.ticket_commands")
        await self.load_extension("cogs.ticket_system")
        
        logger.info("All extensions loaded successfully!")
    
    async def on_ready(self):
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")
        logger.info(f"Connected to {len(self.guilds)} guilds")
        
        # Sync commands with Discord
        await self.tree.sync()
        logger.info("Command tree synced with Discord")
    
    async def close(self):
        if self.db:
            await self.db.close()
        await super().close()
    
    async def on_error(self, event_method, *args, **kwargs):
        logger.error(f"Error in {event_method}: {args} {kwargs}")
        logger.exception("Exception details:")
