from mainn.keys import token,chat_id

from telegram.ext import ApplicationBuilder
import logging
from mainn.message_mate import run

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )


def main():
    app = ApplicationBuilder().token(token).build()
    run()
    app.run_polling()


if __name__ == "__main__":
    main()