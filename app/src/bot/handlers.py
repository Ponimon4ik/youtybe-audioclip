from telegram import Update
from telegram.ext import CallbackContext, ContextTypes

import logger
from src.bot.jobs import job_send_audio
from src.constants.handlers import EXPECTATION, GREETING


async def get_link(update: Update, context: CallbackContext):
    context.job_queue.run_once(
        job_send_audio,
        when=1,
        data=update.message.text,
        chat_id=update.effective_chat.id
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=EXPECTATION
    )
    logger.bot_sent_message(EXPECTATION)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=GREETING
    )
    logger.bot_sent_message(GREETING)
