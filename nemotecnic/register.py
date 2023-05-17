import pandas as pd
from all_funcs.funtions import open_read


archivo = "word_learn.txt"

def show_register():
# devuelve  una palabra  
    palabra = open_read(archivo, True)





datos = {
    'palabras':[palabra ][palabra], # nesesito que la palabra se valla agregando de {palabra}
    'time': []
}

data_frame =  pd.DataFrame(datos)