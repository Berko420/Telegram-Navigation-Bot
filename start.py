import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Setup Messages Directory
    messages_dir = "messages"
    os.makedirs(messages_dir, exist_ok=True)
    
    # Load start message from file
    start_message_path = os.path.join(messages_dir, "start.txt")
    try:
        with open(start_message_path, "r", encoding="utf-8") as file:
            message_text = file.read()
    except FileNotFoundError:
        # If file doesn't exist, create it with a default message
        message_text = "Welcome to the bot!"
        with open(start_message_path, "w", encoding="utf-8") as file:
            file.write(message_text)

    # Send the image first
    logo_path = os.path.join(messages_dir, "image.png")
    try:
        with open(logo_path, "rb") as logo:
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=logo)
    except FileNotFoundError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Image was not found, Make sure image.png is in messages dir.")

    # Send the start message
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)

    # Create buttons
    keyboard = [
        [InlineKeyboardButton("📰 Channel 1", url="https://t.me/Channel1")],
        [InlineKeyboardButton("📰 Channel 2", url="https://t.me/Channel2")],
        [InlineKeyboardButton("📰 Channel 3", url="https://t.me/Channel3")],
        [InlineKeyboardButton("📰 Channel 4", url="https://t.me/Channel4")],
        [InlineKeyboardButton("📰 Group 1 🌐", url="https://t.me/Group1")],
        [InlineKeyboardButton("🌟 Website 1, url="https://t.me/Website1")],
        [InlineKeyboardButton("📞 Contact", url="https://t.me/Contact")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Choose Channel:", reply_markup=reply_markup)
    
    # Log user interaction
    user = update.effective_user
    user_info = f"User ID: {user.id}, Username: {user.username}, Full Name: {user.full_name}\n"
    print(user_info)  # Print user information to terminal
    with open(os.path.join("logs", "UserLOG.txt"), "a", encoding="utf-8") as user_log:
        user_log.write(user_info)
