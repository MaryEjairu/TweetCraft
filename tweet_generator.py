"""
Tweet generation module using Cohere API.
Handles both short tweets and long tweet threads with authentic, human-like content.
"""

import os
import logging
import json
from typing import Dict, List, Optional, Any, Union
import cohere
from config import Config

logger = logging.getLogger(__name__)

class TweetGenerator:
    """Handles tweet generation using Cohere API."""
    
    def __init__(self):
        """Initialize the tweet generator with Cohere client."""
        self.config = Config()
        self.client = cohere.Client(api_key=self.config.cohere_api_key)
        
        # Trazen context for all generated content
        self.trazen_context = """
        Trazen is a curated Web3 discovery and engagement platform currently in its MVP Development stage. Trazen helps users discover and engage with verified Web3 projects across their preferred blockchains and niches.

        Trazen is not a replacement for Twitter or Discord — it's designed to complement them by filtering out noise and giving users only relevant, structured, and verified content.

        Key Features:
        - Personalized onboarding: users select their preferred blockchains and niches, and only see relevant project updates
        - Updates Feed: only registered projects can post updates
        - Projects Page: directory of verified Web3 projects
        - Events Page: curated event listings
        - Jobs & bounty Page: hiring & task board for Web3 roles

"""
Tweet generation module using Cohere API.
Handles both short tweets and long tweet threads with authentic, human-like content.
"""

import os
import logging
import json
from typing import Dict, List, Optional, Any, Union
import cohere
from config import Config

logger = logging.getLogger(__name__)

class TweetGenerator:
    """Handles tweet generation using Cohere API."""
    
    def __init__(self):
        """Initialize the tweet generator with Cohere client."""
        self.config = Config()
        self.client = cohere.Client(api_key=self.config.cohere_api_key)
        
        # Trazen context for all generated content
        self.trazen_context = """
        Trazen is a curated Web3 discovery and engagement platform currently in its MVP Development stage. Trazen helps users discover and engage with verified Web3 projects across their preferred blockchains and niches.

        Trazen is not a replacement for Twitter or Discord — it's designed to complement them by filtering out noise and giving users only relevant, structured, and verified content.

        Key Features:
        - Personalized onboarding: users select their preferred blockchains and niches, and only see relevant project updates
        - Updates Feed: only registered projects can post updates
        - Projects Page: directory of verified Web3 projects
        - Events Page: curated event listings
        - Jobs & bounty Page: hiring & task board for Web3 roles
        - Community Group Chats (coming soon)
        - No open posting from users (yet) — only projects can post
        - Reddit-style interactions (upvotes, comments) to make users feel included without turning it into a spam feed

        Status:
        - Trazen is not launched yet. It's preparing to launch with grant applications (Aptos, Movement Labs, Web3Telegram) in progress
        - A pitch deck, demo video, and landing page are being finalized for the "Demo → Sell → Build" strategy
        - A small team is working on the project, including a product lead, marketing lead, and project manager
        - Founder is currently bootstrapping Trazen with limited resources, while also balancing a nursing program

        Think of Trazen as the "signal" layer in Web3 social — unlike Twitter/X (highway), Trazen is the destination for discovery. Only verified and registered projects can post to prevent scams or noise. Uses a freemium model — free for basic posting, premium unlocks features like analytics, user feedback, and job prioritization.
        """
    
    def analyze_and_generate_short_tweet(self, user_input: str) -> Optional[str]:
        """
        Analyze user input about Trazen updates/progress and generate a relevant short tweet.
        
        Args:
            user_input (str): User's update about Trazen progress, highlights, or current activities
            
        Returns:
            Optional[str]: Generated tweet or None if failed
        """
        try:
            prompt = f"""
            User Update: {user_input}

            Context about Trazen:
            {self.trazen_context}

            Task: Analyze the user's update about Trazen and create a compelling short tweet that shares this progress/insight with the community.
"""
Tweet generation module using Cohere API.
Handles both short tweets and long tweet threads with authentic, human-like content.
"""

import os
import logging
import json
from typing import Dict, List, Optional, Any, Union
import cohere
from config import Config

logger = logging.getLogger(__name__)

class TweetGenerator:
    """Handles tweet generation using Cohere API."""
    
    def __init__(self):
        """Initialize the tweet generator with Cohere client."""
        self.config = Config()
        self.client = cohere.Client(api_key=self.config.cohere_api_key)
        
        # Trazen context for all generated content
        self.trazen_context = """
        Trazen is a curated Web3 discovery and engagement platform currently in its MVP Development stage. Trazen helps users discover and engage with verified Web3 projects across their preferred blockchains and niches.

        Trazen is not a replacement for Twitter or Discord — it's designed to complement them by filtering out noise and giving users only relevant, structured, and verified content.

        Key Features:
        - Personalized onboarding: users select their preferred blockchains and niches, and only see relevant project updates
        - Updates Feed: only registered projects can post updates
        - Projects Page: directory of verified Web3 projects
        - Events Page: curated event listings
        - Jobs & bounty Page: hiring & task board for Web3 roles
        - Community Group Chats (coming soon)
        - No open posting from users (yet) — only projects can post
        - Reddit-style interactions (upvotes, comments) to make users feel included without turning it into a spam feed

        Status:
        - Trazen is not launched yet. It's preparing to launch with grant applications (Aptos, Movement Labs, Web3Telegram) in progress
        - A pitch deck, demo video, and landing page are being finalized for the "Demo → Sell → Build" strategy
        - A small team is working on the project, including a product lead, marketing lead, and project manager
        - Founder is currently bootstrapping Trazen with limited resources, while also balancing a nursing program

        Think of Trazen as the "signal" layer in Web3 social — unlike Twitter/X (highway), Trazen is the destination for discovery. Only verified and registered projects can post to prevent scams or noise. Uses a freemium model — free for basic posting, premium unlocks features like analytics, user feedback, and job prioritization.
        """
    
    def analyze_and_generate_short_tweet(self, user_input: str) -> Optional[str]:
        """
        Analyze user input about Trazen updates/progress and generate a relevant short tweet.
        
        Args:
            user_input (str): User's update about Trazen progress, highlights, or current activities
            
        Returns:
            Optional[str]: Generated tweet or None if failed
        """
        try:
            prompt = f"""
            User Update: {user_input}

            Context about Trazen:
            {self.trazen_context}

            Task: Analyze the user's update about Trazen and create a compelling short tweet that shares this progress/insight with the community.

            Requirements:
            - Maximum 250 characters
            - Sound natural, human, and professional with a casual tone
            - Use minimal emojis (1-2 max, only if they add value)
            - Write from the perspective of someone building/working on Trazen
            - Turn the update into an engaging social media post
            - Avoid obvious AI-generated phrases and buzzwords
            - Make it informative and relatable to the Web3 community
            - Include relevant hashtags only if they feel natural
            - Show genuine progress and insights rather than hype

            Generate only the tweet text, nothing else.
            """
            
            system_message = "You are a Web3 industry professional with deep expertise who shares insights through social media. You write in a professional yet casual tone, sound completely human and natural, and avoid excessive emojis or buzzwords. You understand Trazen's mission in Web3 discovery and can naturally reference it when relevant."
            
            full_prompt = f"{system_message}\n\n{prompt}"
            
            response = self.client.chat(
                model=self.config.cohere_model,
                message=full_prompt,
                max_tokens=100,
                temperature=0.8
            )
            full_prompt = f"{system_message}\n\n{prompt}"
            
            response = self.client.chat(
                model=self.config.cohere_model,
                message=full_prompt,
                max_tokens=100,
                temperature=0.8
            )
            
            tweet = response.text
            if tweet:
                tweet = tweet.strip()
            else:
                return None
            
            # Ensure tweet is within character limit
            if len(tweet) > self.config.short_tweet_limit:
                tweet = tweet[:self.config.short_tweet_limit-3] + "..."
            
            return tweet
            
        except Exception as e:
            logger.error(f"Error generating short tweet: {e}")
            return None
    """
Tweet generation module using Cohere API.
Handles both short tweets and long tweet threads with authentic, human-like content.
"""

import os
import logging
import json
from typing import Dict, List, Optional, Any, Union
import cohere
from config import Config

logger = logging.getLogger(__name__)

class TweetGenerator:
    """Handles tweet generation using Cohere API."""
    
    def __init__(self):
        """Initialize the tweet generator with Cohere client."""
        self.config = Config()
        self.client = cohere.Client(api_key=self.config.cohere_api_key)
        
        # Trazen context for all generated content
        self.trazen_context = """
        Trazen is a curated Web3 discovery and engagement platform currently in its MVP Development stage. Trazen helps users discover and engage with verified Web3 projects across their preferred blockchains and niches.

        Trazen is not a replacement for Twitter or Discord — it's designed to complement them by filtering out noise and giving users only relevant, structured, and verified content.

        Key Features:
        - Personalized onboarding: users select their preferred blockchains and niches, and only see relevant project updates
        - Updates Feed: only registered projects can post updates
        - Projects Page: directory of verified Web3 projects
        - Events Page: curated event listings
        - Jobs & bounty Page: hiring & task board for Web3 roles
        - Community Group Chats (coming soon)
        - No open posting from users (yet) — only projects can post
        - Reddit-style interactions (upvotes, comments) to make users feel included without turning it into a spam feed

        Status:
        - Trazen is not launched yet. It's preparing to launch with grant applications (Aptos, Movement Labs, Web3Telegram) in progress
        - A pitch deck, demo video, and landing page are being finalized for the "Demo → Sell → Build" strategy
        - A small team is working on the project, including a product lead, marketing lead, and project manager
        - Founder is currently bootstrapping Trazen with limited resources, while also balancing a nursing program

        Think of Trazen as the "signal" layer in Web3 social — unlike Twitter/X (highway), Trazen is the destination for discovery. Only verified and registered projects can post to prevent scams or noise. Uses a freemium model — free for basic posting, premium unlocks features like analytics, user feedback, and job prioritization.
        """
    
    def analyze_and_generate_short_tweet(self, user_input: str) -> Optional[str]:
        """
        Analyze user input about Trazen updates/progress and generate a relevant short tweet.
        
        Args:
            user_input (str): User's update about Trazen progress, highlights, or current activities
            
        Returns:
            Optional[str]: Generated tweet or None if failed
        """
        try:
            prompt = f"""
            User Update: {user_input}

            Context about Trazen:
            {self.trazen_context}

            Task: Analyze the user's update about Trazen and create a compelling short tweet that shares this progress/insight with the community.

            Requirements:
            - Maximum 250 characters
            - Sound natural, human, and professional with a casual tone
            - Use minimal emojis (1-2 max, only if they add value)
            - Write from the perspective of someone building/working on Trazen
            - Turn the update into an engaging social media post
            - Avoid obvious AI-generated phrases and buzzwords
            - Make it informative and relatable to the Web3 community
            - Include relevant hashtags only if they feel natural
            - Show genuine progress and insights rather than hype

            Generate only the tweet text, nothing else.
            """
            
            system_message = "You are a Web3 industry professional with deep expertise who shares insights through social media. You write in a professional yet casual tone, sound completely human and natural, and avoid excessive emojis or buzzwords. You understand Trazen's mission in Web3 discovery and can naturally reference it when relevant."
            
            full_prompt = f"{system_message}\n\n{prompt}"
            
            response = self.client.chat(
                model=self.config.cohere_model,
                message=full_prompt,
                max_tokens=100,
                temperature=0.8
            )
            
            tweet = response.text
            if tweet:
                tweet = tweet.strip()
            else:
                return None
            
            # Ensure tweet is within character limit
            if len(tweet) > self.config.short_tweet_limit:
                tweet = tweet[:self.config.short_tweet_limit-3] + "..."
            
            return tweet
            
        except Exception as e:
            logger.error(f"Error generating short tweet: {e}")
            return None
    
    def analyze_and_generate_long_thread(self, user_input: str) -> Optional[List[str]]:
        """
        Analyze user input about Trazen updates/progress and generate a relevant tweet thread.
        
        Args:
            user_input (str): User's update about Trazen progress, highlights, or current activities
            
        Returns:
            Optional[List[str]]: List of tweets forming a thread or None if failed
        """
        try:
            prompt = f"""
            User Update: {user_input}

            Context about Trazen:
            {self.trazen_context}

            Task: Analyze the user's update about Trazen and create an engaging tweet thread that shares this progress/insight with the community in a story format.

            Requirements:
            - 4-8 tweets in the thread
            - Each tweet maximum 250 characters
            - Sound natural, human, and professional with a casual tone
            - Use storytelling to share the journey and insights
            - Minimal emojis (1-2 per tweet max, only if they add value)
            - Write from the perspective of someone building/working on Trazen
            - Turn the update into a compelling narrative about building in Web3
            - Avoid obvious AI-generated phrases and Web3 buzzwords
            - Make it informative and thought-provoking
            - Use thread numbering (1/n, 2/n, etc.) only when it enhances readability
            - Each tweet should flow naturally to tell the complete story
            - Show genuine progress, challenges, and insights rather than just hype
            - Connect the update to broader Web3 trends and lessons

            Format your response as a JSON array of strings, where each string is a tweet.
            Example: ["First tweet text", "Second tweet text", "Third tweet text"]
            """
            
            system_message = "You are a Web3 industry professional with deep expertise who shares insights through social media. You write in a professional yet casual tone, sound completely human and natural, and avoid excessive emojis or buzzwords. You understand Trazen's mission in Web3 discovery and can naturally reference it when relevant. Always respond with valid JSON format."
            
            full_prompt = f"{system_message}\n\n{prompt}"
            
            response = self.client.chat(
                model=self.config.cohere_model,
                message=full_prompt,
                max_tokens=800,
                temperature=0.8
            )
            
            content = response.text
            if not content:
                return None
            
            # Try to parse JSON response
            try:
                result = json.loads(content)
            except json.JSONDecodeError:
                # If not JSON, try to extract content between brackets or split by newlines
                if '[' in content and ']' in content:
                    start = content.find('[')
                    end = content.rfind(']') + 1
                    json_part = content[start:end]
                    try:
                        result = json.loads(json_part)
                    except:
                        # Fallback: split by newlines and create array
                        lines = [line.strip() for line in content.split('\n') if line.strip()]
                        result = lines[:7]  # Max 7 tweets
                else:
                    # Fallback: split by newlines
                    lines = [line.strip() for line in content.split('\n') if line.strip()]
                    result = lines[:7]  # Max 7 tweets
            
            # Extract tweets from various possible JSON structures
            tweets = []
            if isinstance(result, list):
                tweets = result
            elif isinstance(result, dict):
                if 'tweets' in result:
                    tweets = result['tweets']
                elif 'thread' in result:
                    tweets = result['thread']
                else:
                    # Try to get values that are lists
                    for value in result.values():
                        if isinstance(value, list):
                            tweets = value
                            break
            
            # Ensure each tweet is within character limit
            processed_tweets = []
            for tweet in tweets:
                if isinstance(tweet, str):
                    if len(tweet) > self.config.short_tweet_limit:
                        tweet = tweet[:self.config.short_tweet_limit-3] + "..."
                    processed_tweets.append(tweet)
            
            # Limit number of tweets in thread
            if len(processed_tweets) > self.config.long_tweet_thread_limit:
                processed_tweets = processed_tweets[:self.config.long_tweet_thread_limit]
            
            return processed_tweets if processed_tweets else None
            
        except Exception as e:
            logger.error(f"Error generating long tweet thread: {e}")
            return None
    
    def analyze_and_generate_both_formats(self, user_input: str) -> Dict[str, Any]:
        """
        Analyze user input about Trazen and generate both short tweet and long thread formats.
        
        Args:
            user_input (str): User's update about Trazen progress, highlights, or current activities
            
        Returns:
            Dict[str, Any]: Dictionary containing both formats or error information
        """
        result: Dict[str, Any] = {
            "short_tweet": None,
            "long_thread": None,
            "error": None
        }
        
        try:
            # Generate short tweet
            short_tweet = self.analyze_and_generate_short_tweet(user_input)
            if short_tweet:
                result["short_tweet"] = short_tweet
            
            # Generate long thread
            long_thread = self.analyze_and_generate_long_thread(user_input)
            if long_thread:
                result["long_thread"] = long_thread
            
            if not short_tweet and not long_thread:
                result["error"] = "Failed to generate any tweet content"
            
        except Exception as e:
            logger.error(f"Error generating tweets: {e}")
            result["error"] = f"Tweet generation failed: {str(e)}"
        
        return result


