import os
import yfinance as yf
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
import json
import requests
import telebot
import time
import random
import sys
import logging

#loading OpenAI API Key fron .env and setting up API client
load_dotenv()
client=OpenAI()

#Setting up Logging
logging.basicConfig(filename="StockBot.log",format="%(asctime)s %(message)s",filemode="w", level=logging.INFO)

#Loading System Prompt
try:
    with open("./system_prompt", "r") as file:
        SYSTEM_PROMPT=file.read()
except FileNotFoundError:
    print("Error: The file system_prompt was not found.")
    logging.info("Error: The file system_prompt was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    logging.info(f"An error occurred: {e}")

#Telegram Authorization and bot setup
TELEGRAM_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_ID=os.getenv("TELEGRAM_CHAT_ID")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

GREETINGS=["Hello! Please provide a stock symbol for me to analyze.",
           "Howdy! How can I assist your Stock rearch today? Please provide a stock symbol to analyze.",
           "Hey there, I am ready to assist. Please provide a stock symbol for me to assist!"]

#Getting stock data for ChatGPT to analyze
def fetch_stock_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)

    price_history = ticker.history(period="1y")
    if price_history.empty:
        return ""
    info = ticker.info

    # Convert price history to JSON so the LLM can parse it cleanly
    price_json = price_history.reset_index().to_json(orient="records")

    return {
        "ticker": ticker_symbol,
        "history": json.loads(price_json),
        "info": info
    }

#ChatGPT analyzing the stock symbol.
def analyze_with_ai(stock_data):
    user_prompt = f"""
    Analyze the following Yahoo Finance data for ticker {stock_data['ticker']}.

    Price History (1 year):
    {json.dumps(stock_data['history'], indent=2)}

    Fundamentals (Info):
    {json.dumps(stock_data['info'], indent=2)}
    """

    response = client.chat.completions.create(
    # response = client.responses.create(
        model="gpt-5.1",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    input_tokens = response.usage.prompt_tokens
    output_tokens = response.usage.completion_tokens
    print(f"Input tokens: {input_tokens}")
    logging.info(f"Input tokens: {input_tokens}")
    print(f"Output tokens: {output_tokens}")
    logging.info(f"Output tokens: {output_tokens}")

    return response.choices[0].message.content

#Bot Handling the messages sent
@bot.message_handler(func=lambda msg:True)
def Handle_message(message, max_retries=3):
    if str(message.chat.id) != TELEGRAM_ID:
        bot.send_message(message.chat.id, "You are not authorized to use this bot.")
        logging.warning(f"Unauthorized access attempt by chat ID: {message.chat.id}")
        return
    if "hello" in message.text.lower() or "hey" in message.text.lower():
        bot.send_message(message.chat.id, GREETINGS[random.randint(0,len(GREETINGS)-1)])
        logging.info(f"greeting from {message.chat.id}")
        return
    symbol=message.text
    logging.info(f"User: {symbol}")
    print("Fetching Yahoo Finance data...")
    logging.info("Fetching Yahoo Finance data...")
    data = fetch_stock_data(symbol)
    logging.info("Data found in yahoo finance")
    if data == "":
        bot.send_message(message.chat.id, "Not a Stock Symbol, I need a stock symbol to analyze. (i.e. AAPL, NVDA)")
    else:
        for attempt in range(max_retries):
            try:
                bot.reply_to(message, "Analyzing with ChatGPT...")
                print("Analyzing with OpenAI...")
                analysis = analyze_with_ai(data)
                logging.info(f"Bot: {analysis}")
                bot.reply_to(message, analysis, parse_mode="markdown")
                return True
            except (telebot.apihelper.ReadTimeout, requests.exceptions.ReadTimeout):
                print(f"Timeout occurred, retrying... (Attempt {attempt + 1})")
                time.sleep(5)  # Wait for 5 seconds before retrying
        print(f"Failed to send message after {max_retries} attempts.")
        logging.error(f"Failed to send message after {max_retries} attempts.")
        return False
        

def main():
    print("=== Stock Analyzer (yfinance + OpenAI) ===")
    logging.info("Stock Bot service started")
    try:
        bot.polling(non_stop=False)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.info(f"An unexpected error occurred: {e}")
        bot.stop_polling()
        sys.exit(1)


if __name__ == "__main__":
    main()
