import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )

token = "6216170725:AAFyiXk8G7eu9gj0d0zOwr93Sle4fSjqCU4"

async def ():



if __name__ == "__main__":
    aplication = ApplicationBuilder().token(token).build()
   
    aplication.run_polling()