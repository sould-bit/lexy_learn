#%%
#telegram 
from telegram import Update
from telegram.ext import ContextTypes

# modules/
from mainn.chat_proactive import aplication
# from mainn.nemotecnic import algebra
from mainn.nemotecnic.algebra import Notas_nemotecnics
from mainn.keys import chat_id
import random

nota =Notas_nemotecnics()

async def Nemo_Matematicas( context:ContextTypes.DEFAULT_TYPE):
    random_nota = random.choice(list(nota))
    await context.bot.send_message(chat_id =chat_id, text=random_nota) 

# async def Nemo_Matematicas(context: ContextTypes.DEFAULT_TYPE):
#     random_tupla = random.choice(nota)
#     notaa = f"{random_tupla[0]}: {random_tupla[1]}"
#     await context.bot.send_message(chat_id=chat_id, text=notaa)
    
def run():

    send_nemo = aplication.job_queue

    send_nemo.run_repeating(Nemo_Matematicas,interval=5, first=10)
    aplication.run_polling()
    
run()