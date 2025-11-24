# AI Stock Analysis Telegram Bot

This project is a Python-based Telegram bot that provides AI-powered stock analysis. It fetches financial data using `yfinance`, leverages the OpenAI API for in-depth analysis, and delivers the insights directly to a secure, private Telegram chat.

## Features

*   **Real-time Stock Data:** Retrieves historical price data and company fundamentals from Yahoo Finance.
*   **AI-Powered Analysis:** Uses OpenAI's GPT models to interpret financial data and generate comprehensive stock analysis.
*   **Secure Telegram Interface:** Interacts with a user via a Telegram bot, but is secured to only respond to an authorized chat ID.
*   **Customizable AI Behavior:** The AI's analytical style and instructions can be easily modified via a `system_prompt` file.
*   **Robust Logging:** Keeps a log of operations and errors in `StockBot.log`.

## How It Works

1.  A user sends a stock ticker symbol (e.g., `NVDA`) to the Telegram bot.
2.  The bot checks if the message is from an authorized `TELEGRAM_CHAT_ID`.
3.  It then uses the `yfinance` library to fetch 1 year of price history and the company's fundamental information.
4.  This data is formatted and sent to the OpenAI API along with a system prompt that guides the analysis.
5.  The AI's response is streamed back to the user in the Telegram chat.

## Setup and Installation

Follow these steps to set up and run the project locally.

### Prerequisites

*   Python 3.7+
*   An OpenAI API Key
*   A Telegram Bot Token and your personal Chat ID

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <project-directory-name>
```

### 2. Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate
```
*(On Windows, use `.venv\Scripts\activate`)*

### 3. Install Dependencies

Install all the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

The bot requires three secret keys to function. Create a file named `.env` in the root of the project directory and add the following, replacing the placeholder text with your actual credentials.

```env
OPENAI_API_KEY="sk-..."
TELEGRAM_BOT_TOKEN="123456:ABC-DEF1234ghIkl-zyx57W2v1u123456"
TELEGRAM_CHAT_ID="123456789"
```

*   `OPENAI_API_KEY`: Your secret API key from [platform.openai.com](https://platform.openai.com/api-keys).
*   `TELEGRAM_BOT_TOKEN`: To get a token, create a new bot by talking to the [BotFather](https://t.me/botfather) on Telegram.
*   `TELEGRAM_CHAT_ID`: This is your personal Telegram user ID. It ensures that only **you** can interact with the bot. You can get this by sending a message to `@userinfobot` on Telegram.

### 5. Create the System Prompt

The AI's behavior is guided by a system prompt. Create a file named `system_prompt` in the root directory. Paste the instructions you want the AI to follow into this file. For example:

```
You are a sophisticated stock analysis assistant. Analyze the provided yfinance data. Offer a balanced view, highlighting both bullish and bearish cases. Conclude with a final summary and a recommendation on whether to buy, hold, or sell, based purely on the data provided.
```

## Usage

Once all the setup steps are complete, you can start the bot by running the `Bot.py` script:

```bash
python Bot.py
```

The terminal will display `=== Stock Analyzer (yfinance + OpenAI) ===`, and the bot is now active. Send it a stock ticker in your Telegram chat, and it will reply with the analysis.

To stop the bot, press `CTRL+C` in the terminal.

## Project File Structure

*   `Bot.py`: The main script containing all the bot logic, data fetching, and AI integration.
*   `requirements.txt`: A list of all Python dependencies required for the project.
*   `system_prompt`: A text file containing the system-level instructions for the OpenAI model.
*   `.env`: Stores secret environment variables (API keys, tokens). This file is ignored by Git.
*   `StockBot.log`: Log file for the bot's operations and errors.