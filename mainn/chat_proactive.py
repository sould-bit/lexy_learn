from mainn.keys import token
from telegram.ext import Application
# esta construccion permitira tomar los modulos para hacer los chats proactivos 

aplication = Application.builder().token(token).build()