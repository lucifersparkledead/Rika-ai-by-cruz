import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'NYRA'))

import random
import logging
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import LOG_CHAT_ID
from utils.db import add_served_chat, delete_served_chat

welcome_photo = "https://files.catbox.moe/qxxbe3.jpg"
left_photos = [
    "https://files.catbox.moe/yp8yby.mp4",
    "https://files.catbox.moe/g4b0px.mp4"
]


async def log_user_start(message: types.Message):
    try:
        await add_served_chat(message.chat.id, "private")
        await message.bot.send_message(
            LOG_CHAT_ID,
            f"🌸 New User Started Nyra:\n"
            f"Name: {message.from_user.full_name}\n"
            f"Username: @{message.from_user.username or 'N/A'}\n"
            f"User ID: {message.from_user.id}"
        )
    except Exception as e:
        logging.error(f"Error logging user start: {e}")


async def log_bot_added(message: types.Message):
    try:
        await add_served_chat(message.chat.id, message.chat.type)
        await message.bot.send_message(
            LOG_CHAT_ID,
            f"➕ Nyra added to group:\n"
            f"Group: {message.chat.title}\n"
            f"ID: {message.chat.id}\n"
            f"Added by: {message.from_user.full_name if message.from_user else 'Unknown'}"
        )
    except Exception as e:
        logging.error(f"Error logging bot added: {e}")


async def log_bot_removed(update: types.ChatMemberUpdated):
    try:
        await delete_served_chat(update.chat.id)
        from aiogram import Bot
        await update.bot.send_message(
            LOG_CHAT_ID,
            f"➖ Nyra removed from group:\n"
            f"Group: {update.chat.title}\n"
            f"ID: {update.chat.id}"
        )
    except Exception as e:
        logging.error(f"Error logging bot removed: {e}")
