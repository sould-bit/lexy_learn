from telegram import Update
from telegram.ext import CommandHandler, ContextTypes,MessageHandler,filters,CallbackContext

#import connector sql
from conector_sql import connect_db

#import enshure
from insert_user import ensure_user_exists

#import ejecucion de sql (logica del bot(en cuanto a las palabras))
from ejecucion_sql_tables import get_next_element
import asyncio

from ollama_cht_model import response_ollama





async def get_slang(update: Update, context:ContextTypes.DEFAULT_TYPE):
    name = update.effective_chat.first_name
    id_user = update.message.from_user.id
    print(f"obteniedno id {id_user}")
    
    #verificamos si el usuario ya esta en la base de datos 
    ensure_user_exists(id_user,name)
    
    # determinar si el usuario es premiun 
    
    conn =connect_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT is_premium FROM users WHERE user_id = %s', (id_user,))
    (is_premium,) = cursor.fetchone()
    print(f"user_id: {id_user} is premiun:{is_premium}")
    conn.close()
    
    palabra = get_next_element(id_user,is_premium,'american_slang')
    # Convierte los elementos a cadenas y únelos con una nueva línea
    elements_text = [str(element) for element in palabra]

    # mensaje = add_word(palabra)
    print("enviando mensaje")
    

    await update.message.reply_text(f"{'\n\n'.join(elements_text)}")
    
    
async def get_word(update: Update, context:ContextTypes.DEFAULT_TYPE):
    name = update.effective_chat.first_name
    id_user = update.message.from_user.id
    print(f"obteniedno id {id_user}")
    
    #verificamos si el usuario ya esta en la base de datos 
    ensure_user_exists(id_user,name)
    
    # determinar si el usuario es premiun 
    
    conn =connect_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT is_premium FROM users WHERE user_id = %s', (id_user,))
    (is_premium,) = cursor.fetchone()
    print(f"user_id: {id_user} is premiun:{is_premium}")
    conn.close()
    
    palabra = get_next_element(id_user,is_premium,'word')
    # Convierte los elementos a cadenas y únelos con una nueva línea
    elements_text = [str(element) for element in palabra]

    # mensaje = add_word(palabra)
    print("enviando mensaje")
    

    await update.message.reply_text(f"{'\n\n'.join(elements_text)}")
    
    
    
async def handler_response(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    user_id = update.message.from_user.id
    response_ollama_user= response_ollama(str(user_message))
    print(f"User ID: {user_id} - Message: {user_message}")
    
    # Responder al usuario
    await update.message.reply_text(f"{response_ollama_user}")


mensaje_slang = CommandHandler('get_slang', get_slang)
mensaje = CommandHandler('get_words', get_word)
response = MessageHandler(filters.TEXT & ~filters.COMMAND, handler_response)

#remove = CommandHandler('remove', remove_words)
