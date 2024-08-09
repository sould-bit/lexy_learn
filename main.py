from mainn.keys import token,chat_id

from telegram.ext import ApplicationBuilder
import logging
from message.message_english import mensaje, response,mensaje_slang
#from message.message_english import remove

    

def main():
    logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )
    app = ApplicationBuilder().token(token).build()
    #app.add_handler(mensaje)# manejaro de get_word llamado para obtener la palabra
    app.add_handler(mensaje)# manejaro de get_slang llamado para obtener la jerga
    app.add_handler(mensaje_slang)# manejaro de get_slang llamado para obtener la jerga
    #app.add_handler(remove)
    app.add_handler(response)
    app.run_polling()


if __name__ == "__main__":
    main()
    
    