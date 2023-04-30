from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from nemotecnic.world_english import get_random





async def message_word_english(update: Update, context:ContextTypes.DEFAULT_TYPE):
    mensaje = get_random()
    print("enviando mensaje")
    await context.bot.sendMessage(chat_id=update.effective_chat.id, text=mensaje)
    




mensaje = CommandHandler('english', message_word_english)
