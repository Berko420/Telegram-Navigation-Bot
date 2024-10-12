# File: main.py
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN
from start import start_command
from help import help_command

# Setup Logs Directory
logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)

# Setting up logging
logging.basicConfig(
    filename=os.path.join(logs_dir, "DebugLOG.txt"),
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    if not BOT_TOKEN:
        raise ValueError("The BOT_TOKEN is not set in the config file. Please make sure it is properly configured.")

    # Initialize Bot Application
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Add Handlers
    # Ensure messages and logs directories exist
    messages_dir = "messages"
    logs_dir = "logs"
    os.makedirs(messages_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Run the bot
    app.run_polling()