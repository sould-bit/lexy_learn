from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from mainn.chat_proactive import app





async def message_word_english(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print("enviando mensaje")
    await context.bot.sendMessage(chat_id=update.effective_chat.id, text=" hello wey")
    




mensaje = CommandHandler('english', message_word_english)
