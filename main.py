from mainn.keys import token,chat_id

from telegram.ext import ApplicationBuilder
import logging
from message.message_mate import run
from message.message_english import mensaje


def main():
    logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )
    app = ApplicationBuilder().token(token).build()
    app.add_handler(mensaje)

    app.run_polling()


if __name__ == "__main__":
    main()