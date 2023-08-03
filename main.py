from mainn.keys import token,chat_id

from telegram.ext import ApplicationBuilder
import logging
from message.message_english import mensaje
from message.message_english import remove

    

def main():
    logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )
    app = ApplicationBuilder().token(token).build()
    app.add_handler(mensaje)
    app.add_handler(remove)

    app.run_polling()


if __name__ == "__main__":
    main()
    
    