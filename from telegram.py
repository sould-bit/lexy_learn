from telegram.ext import ContextTypes, Application
token = "6216170725:AAFyiXk8G7eu9gj0d0zOwr93Sle4fSjqCU4"
async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id="1903762283"
, text='One message every minute')

application = Application.builder().token(token).build()
job_queue = application.job_queue

job_queue.run_repeating(callback_minute, interval=5, first=10)

application.run_polling()