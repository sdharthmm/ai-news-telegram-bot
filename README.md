# AI News Telegram Bot

A Telegram bot that fetches news articles based on a keyword and uses a **local AI model (LLM)** to generate a clean headline and summary before posting it to Telegram.

Instead of sending long raw news articles, the bot uses AI to create a **short, readable news update**.

This project demonstrates how to combine:

* Telegram Bot API
* News APIs
* Local Large Language Models (LLMs)
* Python automation

---

# What This Bot Does

When a user sends a **keyword** to the Telegram bot:

Example:

AI
Crypto
Space

The bot will:

1. Fetch a news article related to that keyword.
2. Send the article text to a **local AI model**.
3. The AI generates:

   * A **catchy headline**
   * A **short description**
4. The formatted result is sent back to Telegram.

Example output:

📰 AI Dating Bots Are Becoming Popular

People are increasingly forming emotional connections with AI-powered companions, raising new questions about relationships and technology.

---

# How The System Works

Telegram Message
↓
Keyword Received
↓
News API Fetches Article
↓
Local AI Model Processes Article
↓
Title + Summary Generated
↓
Message Sent Back to Telegram

The AI runs **locally on your computer**, meaning no paid AI APIs are required.

---

# Technologies Used

Python

Telegram Bot API

GPT4All (local LLM runtime)

Qwen 2.5 Coder 7B (GGUF model)

News API

---

# Project Structure

ai-news-telegram-bot/

ai_simplifier/
Handles AI processing and summarization

news_fetcher/
Fetches news articles from the API

telegram_bot/
Handles Telegram message processing

models/
Folder where the AI model file will be placed

main.py
Main entry point that runs the bot

config.py
Loads environment variables

requirements.txt
Python dependencies

---

# Requirements

You need:

Python 3.9 or higher

Git

Internet connection (for fetching news)

At least **8 GB RAM recommended** to run the AI model.

---

# Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-news-telegram-bot.git
cd ai-news-telegram-bot
```

---

# Step 2 — Create a Python Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 4 — Download the AI Model

Download the following model:

Qwen2.5-Coder-7B-Instruct (GGUF)

Example source:

https://gpt4all.io/models/

After downloading, place the model file inside:

models/

Final folder should look like:

models/
qwen2.5-coder-7b-instruct-q4_0.gguf

---

# Step 5 — Create Environment Variables

Create a file called:

.env

Inside the project root folder.

Add this:

BOT_TOKEN=your_telegram_bot_token
NEWS_API_KEY=your_news_api_key

---

# How To Get A Telegram Bot Token

1. Open Telegram
2. Search for **BotFather**
3. Run:

/newbot

4. Follow the instructions
5. Copy the bot token and place it inside `.env`

Example:

BOT_TOKEN=123456789:ABCXYZTOKEN

---

# How To Get A News API Key

1. Go to:

https://newsapi.org

2. Create a free account

3. Generate an API key

4. Add it to your `.env` file.

Example:

NEWS_API_KEY=abcdef123456

---

# Step 6 — Run The Bot

Start the bot with:

```bash
python main.py
```

If everything is configured correctly, the terminal will show:

Bot started...

---

# How To Use The Bot

Open Telegram and send a keyword to the bot.

Example:

AI
Crypto
Technology
Space

The bot will:

Fetch a news article
Generate an AI headline
Generate a short summary
Send the result to Telegram

---

# Example Output

📰 AI Companions Are Changing Relationships

AI-powered companion apps are becoming more common, with users forming emotional connections with chatbots and virtual partners.

---

# Security Notes

This project uses environment variables to store sensitive data.

The following files are **not committed to GitHub**:

.env
models/

This prevents leaking:

Telegram bot tokens
API keys
Large AI model files

---

# Future Improvements

Planned upgrades for this project include:

Docker container support

CI/CD pipeline deployment

Automatic news posting on schedule

Multiple article summarization

Adding article images to Telegram posts

---

# License

MIT License

---

# Author

Developed as a learning project to explore **AI automation with Telegram bots and local LLMs**.
