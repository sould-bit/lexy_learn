from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from nemotecnic.add_list import add_word, main
from nemotecnic.world_english import get_random
from nemotecnic.remove_top10 import remove_top
import asyncio





async def message_word_english(update: Update, context:ContextTypes.DEFAULT_TYPE):
    a = get_random()
    palabra = main()
    # mensaje = add_word(palabra)
    print("enviando mensaje")
    await context.bot.sendMessage(chat_id=update.effective_chat.id, text=palabra)
    
    

async def remove_words(update: Update, context:ContextTypes.DEFAULT_TYPE):
    name = update.effective_chat.first_name
    remove = remove_top(name)
    print("remove")
    await context.bot.sendMessage(chat_id=update.effective_chat.id, text=remove)


mensaje = CommandHandler('english', message_word_english)

remove = CommandHandler('remove', remove_words)
