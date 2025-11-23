# Stock Analyzer with OpenAI and Telegram Bot

This project implements a Telegram bot that allows users to get stock analysis powered by Yahoo Finance data and OpenAI's language models.

## Features

*   **Stock Data Fetching:** Retrieves historical price data and fundamental information for stock tickers using `yfinance`.
*   **AI-Powered Analysis:** Utilizes OpenAI's API to analyze stock data and provide insights.
*   **Telegram Integration:** Interacts with users through a Telegram bot interface.
*   **Environment Variable Management:** Securely loads API keys and tokens using `python-dotenv`.

## Setup

Follow these steps to set up and run the project locally.

### Prerequisites

*   Python 3.x installed on your system.
*   A virtual environment is highly recommended.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create a virtual environment (if you haven't already):**
    ```bash
    python3 -m venv .venv
    ```

3.  **Activate the virtual environment:**
    *   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .venv\Scripts\activate
        ```

4.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Environment Variables

Create a file named `.env` in the root directory of your project and add the following variables:

```
OPENAI_API_KEY="your_openai_api_key_here"
TELEGRAM_BOT_TOKEN="your_telegram_bot_token_here"
TELEGRAM_CHAT_ID="your_telegram_chat_id_here"
```

*   **`OPENAI_API_KEY`**: Your API key from OpenAI.
*   **`TELEGRAM_BOT_TOKEN`**: Obtain this by creating a new bot with BotFather on Telegram.
*   **`TELEGRAM_CHAT_ID`**: The chat ID where your bot will communicate. You can get this by sending a message to your bot and then navigating to `https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/getUpdates` in your browser.

### System Prompt

The AI's behavior is guided by a system prompt stored in the `system_prompt` file. You can customize this file to refine the AI's analysis style and instructions.

## Usage

To start the Telegram bot, run the `finance.py` script:

```bash
python finance.py
```

The bot will start polling for messages. You can then interact with it via Telegram by sending it stock symbols (e.g., `AAPL`, `GOOGL`).

## File Structure

*   `.env`: Stores environment variables (API keys, tokens).
*   `.gitignore`: Specifies files and directories to be ignored by Git.
*   `finance.py`: The main script containing the bot logic, stock data fetching, and AI analysis integration.
*   `requirements.txt`: Lists all Python dependencies required for the project.
*   `system_prompt`: Contains the system-level instructions for the OpenAI model.
*   `testing.py`: (Optional) A script used for testing various components during development.

---
