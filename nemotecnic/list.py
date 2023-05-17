#%%
from funtions import open_write, open_read, open_readlines, ciclo_top_10
from world_english import get_random
import os
def app(user_top):
    name_arch  = user_top + ".txt"
    if os.path.isfile(name_arch):
        data = open_readlines(name_arch)
        # antes de agregar los datos , nesesitamos validar si ya tiene mas de 7 words 
        count_words =len(data)
        print("leido")
        if count_words > 174:
            read = open_read(name_arch,split=True)
            print(ciclo_top_10(read))


app("Jasbleidi")
