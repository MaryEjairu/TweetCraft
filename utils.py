"""
Utility functions for the Tweet Generator Bot.
Helper functions for formatting, validation, and data processing.
"""

import re
import html
from typing import List, Optional

def sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent issues and improve processing.
    
    Args:
        text (str): Raw user input
        
    Returns:
        str: Sanitized text
    """
    if not text:
        return ""
    
    # Remove HTML entities and normalize
    text = html.unescape(text)
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    # Limit length to prevent extremely long inputs
    if len(text) > 500:
        text = text[:500] + "..."
    
    return text

def format_tweet_response(short_tweet: Optional[str], long_thread: Optional[List[str]], user_update: str) -> str:
    """
    Format the response message with generated tweets. 
Args:
        short_tweet (Optional[str]): Generated short tweet
        long_thread (Optional[List[str]]): Generated tweet thread
        user_update (str): Original user update
        
    Returns:
        str: Formatted response message
    """
"""
Utility functions for the Tweet Generator Bot.
Helper functions for formatting, validation, and data processing.
"""

import re
import html
from typing import List, Optional

def sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent issues and improve processing.
    
    Args:
        text (str): Raw user input
        
    Returns:
        str: Sanitized text
    """
    if not text:
        return ""
    
    # Remove HTML entities and normalize
    text = html.unescape(text)
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    # Limit length to prevent extremely long inputs
    if len(text) > 500:
        text = text[:500] + "..."
    
    return text

def format_tweet_response(short_tweet: Optional[str], long_thread: Optional[List[str]], user_update: str) -> str:
    """
    Format the response message with generated tweets.
    
    Args:
        short_tweet (Optional[str]): Generated short tweet
        long_thread (Optional[List[str]]): Generated tweet thread
        user_update (str): Original user update
        
    Returns:
        str: Formatted response message
    """
    response_parts = []
    
    response_parts.append(f"🎯 **Tweets from your update:**\n")
    
    # Add short tweet section
    if short_tweet:
        char_count = len(short_tweet)
        response_parts.append(f"📝 **Short Tweet:**\n{short_tweet}\n📊 *{char_count}/250 characters*\n")
    else:
        response_parts.append("📝 **Short Tweet:** ❌ Generation failed\n")
    
    # Add separator
    response_parts.append("➖➖➖➖➖➖➖➖➖➖\n")
"""
Utility functions for the Tweet Generator Bot.
Helper functions for formatting, validation, and data processing.
"""

import re
import html
from typing import List, Optional

def sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent issues and improve processing.
    
    Args:
        text (str): Raw user input
        
    Returns:
        str: Sanitized text
    """
    if not text:
        return ""
    
    # Remove HTML entities and normalize
    text = html.unescape(text)
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    # Limit length to prevent extremely long inputs
    if len(text) > 500:
        text = text[:500] + "..."
    
    return text

def format_tweet_response(short_tweet: Optional[str], long_thread: Optional[List[str]], user_update: str) -> str:
    """
    Format the response message with generated tweets.
    
    Args:
        short_tweet (Optional[str]): Generated short tweet
        long_thread (Optional[List[str]]): Generated tweet thread
        user_update (str): Original user update
        
    Returns:
        str: Formatted response message
    """
    response_parts = []
    
    response_parts.append(f"🎯 **Tweets from your update:**\n")
    
    # Add short tweet section
    if short_tweet:
        char_count = len(short_tweet)
        response_parts.append(f"📝 **Short Tweet:**\n{short_tweet}\n📊 *{char_count}/250 characters*\n")
    else:
        response_parts.append("📝 **Short Tweet:** ❌ Generation failed\n")
    
    # Add separator
    response_parts.append("➖➖➖➖➖➖➖➖➖➖\n")
    
    # Add long thread section
    if long_thread and len(long_thread) > 0:
        response_parts.append(f"🧵 **Tweet Thread ({len(long_thread)} tweets):**\n")
        
        for i, tweet in enumerate(long_thread, 1):
            char_count = len(tweet)
            response_parts.append(f"**{i}.** {tweet}\n*{char_count}/250 characters*\n")
    else:
        response_parts.append("🧵 **Tweet Thread:** ❌ Generation failed\n")
    
    response_parts.append("\n💡 *Copy and paste any tweets you like!*")
erate(long_thread, 1):
            char_count = len(tweet)
            response_parts.append(f"**{i}.** {tweet}\n*{char_count}/250 characters*\n")
    else:
        response_parts.append("🧵 **Tweet Thread:** ❌ Generation failed\n")
    
    response_parts.append("\n💡 *Copy and paste any tweets you like!*")
    
    return "\n".join(response_parts)

def validate_tweet_length(tweet: str, max_length: int = 280) -> bool:
    """
    Validate if tweet is within character limit.
    
    Args:
        tweet (str): Tweet text
        max_length (int): Maximum allowed characters
        
    Returns:
        bool: True if valid length, False otherwise
    """
    return len(tweet) <= max_length

character limit.
    
    Args:
        tweet (str): Tweet text
        max_length (int): Maximum allowed characters
        
    Returns:
        bool: True if valid length, False otherwise
    """
    return len(tweet) <= max_length

def truncate_tweet(tweet: str, max_length: int = 280) -> str:
    """
    Truncate tweet to fit within character limit.
    
    Args:
        tweet (str): Tweet text
        max_length (int): Maximum allowed characters
        
    Returns:
        str: Truncated tweet
    """
    if len(tweet) <= max_length:
        return tweet
    
    # Truncate and add ellipsis
    truncated = tweet[:max_length - 3] + "..."
    return truncated

        tweet (str): Tweet text
        max_length (int): Maximum allowed characters
        
    Returns:
        str: Truncated tweet
    """
    if len(tweet) <= max_length:
        return tweet
    
    # Truncate and add ellipsis
    truncated = tweet[:max_length - 3] + "..."
    return truncated

def count_tweet_characters(tweet: str) -> int:
    """
    Count characters in a tweet (useful for display).
    
    Args:
        tweet (str): Tweet text
        
    Returns:
        int: Character count
    """
    return len(tweet)

str) -> int:
    """
    Count characters in a tweet (useful for display).
    
    Args:
        tweet (str): Tweet text
        
    Returns:
        int: Character count
    """
    return len(tweet)

def extract_hashtags(text: str) -> List[str]:
    """
    Extract hashtags from text.
    
    Args:
        text (str): Text to extract hashtags from
        
    Returns:
        List[str]: List of hashtags without # symbol
    """
    hashtag_pattern = r'#(\w+)'
    hashtags = re.findall(hashtag_pattern, text)
    return hashtags

    Args:
        text (str): Text to extract hashtags from
        
    Returns:
        List[str]: List of hashtags without # symbol
    """
    hashtag_pattern = r'#(\w+)'
    hashtags = re.findall(hashtag_pattern, text)
    return hashtags

def extract_mentions(text: str) -> List[str]:
    """
    Extract mentions from text.
    
    Args:
        text (str): Text to extract mentions from
        
    Returns:
        List[str]: List of mentions without @ symbol
    """
    mention_pattern = r'@(\w+)'
    mentions = re.findall(mention_pattern, text)
    return mentions

        List[str]: List of hashtags without # symbol
    """
    hashtag_pattern = r'#(\w+)'
    hashtags = re.findall(hashtag_pattern, text)
    return hashtags

def extract_mentions(text: str) -> List[str]:
    """
    Extract mentions from text.
    
    Args:
        text (str): Text to extract mentions from
        
    Returns:
        List[str]: List of mentions without @ symbol
    """
    mention_pattern = r'@(\w+)'
    mentions = re.findall(mention_pattern, text)
    return mentions

def format_error_message(error_type: str, details: str = "") -> str:
    """
    Format error messages for user display.
    
    Args:
        error_type (str): Type of error
        details (str): Additional error details
        
    Returns:
        str: Formatted error message
    """
ions from
        
    Returns:
        List[str]: List of mentions without @ symbol
    """
    mention_pattern = r'@(\w+)'
    mentions = re.findall(mention_pattern, text)
    return mentions

def format_error_message(error_type: str, details: str = "") -> str:
    """
    Format error messages for user display.
    
    Args:
        error_type (str): Type of error
        details (str): Additional error details
        
    Returns:
        str: Formatted error message
    """
    error_messages = {
        "rate_limit": "⏳ You've reached the rate limit. Please wait before trying again.",
        "api_error": "🔧 There's an issue with our tweet generation service. Please try again later.",
        "invalid_input": "❌ Please provide a valid topic for tweet generation.",
        "generation_failed": "❌ Tweet generation failed. Please try a different topic or try again later.",
        "network_error": "🌐 Network connection issue. Please check your connection and try again."
    }
    
    base_message = error_messages.get(error_type, "❌ An unexpected error occurred.")
    
    if details:
        return f"{base_message}\n\n*Details: {details}*"
    
    return base_message



