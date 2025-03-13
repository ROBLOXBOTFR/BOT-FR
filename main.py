import asyncio
import os
import logging
from dotenv import load_dotenv
from bot import TicketBot

# Load environment variables from .env file if it exists
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Get the bot token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    logger.error("No DISCORD_TOKEN found in environment variables!")
    exit(1)

async def main():
    # Create and run the bot
    bot = TicketBot()
    try:
        await bot.start(TOKEN)
    except KeyboardInterrupt:
        logger.info("Bot is shutting down...")
        await bot.close()
    except Exception as e:
        logger.error(f"Error running bot: {e}")
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
