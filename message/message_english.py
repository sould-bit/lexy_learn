from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from nemotecnic.add_list import add_word, main
from nemotecnic.world_english import get_random





async def message_word_english(update: Update, context:ContextTypes.DEFAULT_TYPE):
    a = get_random()
    palabra = main()
    # mensaje = add_word(palabra)
    print("enviando mensaje")
    await context.bot.sendMessage(chat_id=update.effective_chat.id, text=palabra)
    
    




mensaje = CommandHandler('english', message_word_english)
