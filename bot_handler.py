"""
Telegram bot message and command handlers.
Handles user interactions and coordinates tweet generation.
"""

import logging
from typing import Dict
from datetime import datetime, timedelta
from telebot import TeleBot, types
from tweet_generator import TweetGenerator
from utils import format_tweet_response, sanitize_input

logger = logging.getLogger(__name__)

class BotHandlers:
    """Handles all bot interactions and commands."""
    
    def __init__(self, bot: TeleBot):
        """Initialize the bot handlers."""
        self.bot = bot
        self.tweet_generator = TweetGenerator()
        self.user_request_tracker: Dict[int, list] = {}  # Track user requests for rate limiting
        self.rate_limit_hours = 1
        self.max_requests_per_hour = 10
    
    def _check_rate_limit(self, user_id: int) -> bool:
        """
        Check if user has exceeded rate limit.
        
        Args:
            user_id (int): Telegram user ID
            
        Returns:
            bool: True if user can make request, False if rate limited
        """
        now = datetime.now()
        cutoff_time = now - timedelta(hours=self.rate_limit_hours)
        
        # Initialize user tracking if not exists
        if user_id not in self.user_request_tracker:
            self.user_request_tracker[user_id] = []
        
        # Remove old requests
        self.user_request_tracker[user_id] = [
            req_time for req_time in self.user_request_tracker[user_id]
            if req_time > cutoff_time
        ]
        
        # Check if under limit
        if len(self.user_request_tracker[user_id]) >= self.max_requests_per_hour:
            return False
        
        # Add current request
        self.user_request_tracker[user_id].append(now)
        return True
    
    def start_command(self, message):
        """Handle /start command."""
        welcome_message = """
🤖 Welcome to the Trazen Tweet Assistant!

Share your Trazen updates, progress, or insights with me and I'll turn them into engaging tweets for your community.

📝 **What I do:**
• Analyze your updates about Trazen's development
• Create authentic tweets from your progress reports
• Turn your insights into compelling social content

**Commands:**
• `/help` - Show detailed help
• `/short [your update]` - Generate only a short tweet
• `/long [your update]` - Generate only a tweet thread
• Just send your update - Get both formats!
