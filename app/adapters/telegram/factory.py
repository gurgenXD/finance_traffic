import logging
from telegram import Update
from typing import TYPE_CHECKING
from telegram.ext import (
    Application,
    filters,
    MessageHandler,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)


if TYPE_CHECKING:
    from telegram.ext import Application


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text
    )

TOKEN = "5477772752:AAFkfautVujmWVUI0PGdFU2Aa2ONYPGHzb8"


def create_app() -> "Application":
    """Создать приложение TelegramBot."""
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    return application
