"""
Configuration module for the Telegram Tweet Generator Bot.
Handles environment variables and application settings.
"""

import os
from typing import Optional

class Config:
    """Configuration class for bot settings and API keys."""
    
    def __init__(self):
        """Initialize configuration from environment variables."""
        # Telegram Bot Token
        self.telegram_token: Optional[str] = os.getenv("TELEGRAM_BOT_TOKEN")
        
        # Cohere API Key
        self.cohere_api_key: Optional[str] = os.getenv("COHERE_API_KEY")
        
        # Cohere Model Configuration
        self.cohere_model: str = "command-r-plus"
        
        # Tweet length limits
        self.short_tweet_limit: int = 250  # Leave room for engagement
        self.long_tweet_thread_limit: int = 8  # Maximum number of tweets in a thread
        
        # Rate limiting settings
        self.max_requests_per_user_per_hour: int = 10
        
        # Bot behavior settings
        self.default_response_timeout: int = 30  # seconds
        
    def validate(self) -> bool:
        """Validate that all required configuration is present."""
        if not self.telegram_token:
            return False
        if not self.cohere_api_key:
            return False
        return True
