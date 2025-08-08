"""
Telegram Tweet Generator Bot
Main application entry point that starts the bot and handles updates.
"""

import logging
import os
from telebot import TeleBot, types
from config import Config
from bot_handlers import BotHandlers

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Main function to start the Telegram bot."""
    try:
        # Initialize configuration
        config = Config()
        
        # Validate required environment variables
        if not config.telegram_token:
            logger.error("TELEGRAM_BOT_TOKEN not found in environment variables")
            return
            
        if not config.cohere_api_key:
            logger.error("COHERE_API_KEY not found in environment variables")
            return
        
        # Create bot instance
        bot = TeleBot(config.telegram_token)
        
        # Initialize bot handlers
        bot_handlers = BotHandlers(bot)
        
        # Register handlers
        @bot.message_handler(commands=['start'])
        def start_command(message):
            bot_handlers.start_command(message)
            
        @bot.message_handler(commands=['help'])
        def help_command(message):
            bot_handlers.help_command(message)
            
        @bot.message_handler(commands=['short'])
        def short_tweet_command(message):
            bot_handlers.short_tweet_command(message)
            
        @bot.message_handler(commands=['long'])
        def long_tweet_command(message):
            bot_handlers.long_tweet_command(message)
            
        @bot.message_handler(func=lambda message: True)
        def handle_message(message):
            bot_handlers.handle_message(message)
        
        logger.info("Starting Tweet Generator Bot...")
        
        # Start the bot
        bot.polling(non_stop=True, interval=0, timeout=20)
        
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")

if __name__ == '__main__':
    main()
