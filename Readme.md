# Trazen TweetCraft Bot

A Telegram bot built in Python that generates authentic short and long tweets for the Web3 community using OpenAI’s GPT-3.5 API. This bot listens to user messages and replies with creative tweet ideas tailored to the user’s input — perfect for Web3 projects, communities, and enthusiasts looking for engaging content.

---

## Features

- Responds to user messages on Telegram with tweet suggestions  
- Generates both short tweets (under 280 characters) and longer tweet threads  
- Uses OpenAI GPT-3.5 API for natural, human-like content generation  
- Easy setup with environment variables for API keys  
- Hosted and runnable on Replit or any Python environment

---

## How It Works

1. A user sends a topic or prompt message to the Telegram bot.  
2. The bot forwards the prompt to the OpenAI GPT-3.5 API.  
3. GPT-3.5 generates 3 tweet ideas or threads based on the prompt.  
4. The bot replies to the user on Telegram with the generated tweets.

---

## Tech Stack

- Python 3  
- [python-telegram-bot](https://python-telegram-bot.org/) library  
- OpenAI GPT-3.5 API  
- Hosted on Replit (or any Python-compatible environment)

---

## Setup & Installation

1. **Create a Telegram bot**  
   - Talk to [BotFather](https://telegram.me/BotFather) on Telegram  
   - Create a new bot and get your bot token

2. **Get OpenAI API key**  
   - Sign up at [OpenAI](https://openai.com)  
   - Generate an API key from your account dashboard

3. **Clone this repo**  
   ```bash
   git clone https://github.com/yourusername/trazen-tweetcraft-bot.git
   cd trazen-tweetcraft-bot

4. Set environment variables
Create a .env file in the root folder with:

TELEGRAM_BOT_TOKEN=your-telegram-bot-token
OPENAI_API_KEY=your-openai-api-key


5. Install dependencies

pip install -r requirements.txt


6. Run the bot

python main.py


7. Start chatting
Open Telegram, search your bot’s username, and send it a message to get tweet ideas!




---

Usage

Send any topic or keyword related to Web3, blockchain, NFTs, or your project.

The bot will respond with 3 short tweet ideas or a longer tweet thread based on your input.

Example message: Tell me tweets about NFT communities



---

Notes

The bot requires internet access and valid API keys to function.

OpenAI API usage may incur costs depending on your subscription plan.

The bot currently supports English-language tweets only.



---

License

MIT License © [Trazen]


---

Contact

For questions or collaboration, contact [maryejairu1@gmail.com] or open an issue on GitHub.


---

Built with ❤️ by [Mary]
