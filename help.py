# File: help.py
import os
from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Setup Messages Directory
    messages_dir = "messages"
    os.makedirs(messages_dir, exist_ok=True)

    # Load help message from file
    help_message_path = os.path.join(messages_dir, "help.txt")
    try:
        with open(help_message_path, "r", encoding="utf-8") as file:
            help_text = file.read()
    except FileNotFoundError:
        # If file doesn't exist, create it with a default message
        help_text = "This is the help message. You can customize this message."
        with open(help_message_path, "w", encoding="utf-8") as file:
            file.write(help_text)

    # Send a pop-up message (alert) using answer callback query
    if update.callback_query:
        query = update.callback_query
        await query.answer(help_text, show_alert=True)
    else:
        # In case it is not a callback query, just send a regular message
        await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)
