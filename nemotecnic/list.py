#%%
import os

nombre_archivo = "Jhon.txt"
tamaño = os.path.getsize(nombre_archivo)

print(f"El tamaño del archivo '{nombre_archivo}' es {tamaño} bytes.")


#%%
from funtions import open_write, open_read, open_readlines, ciclo_top_10


a = open_readlines("Jhon.txt")
b =  open_read("Jhon.txt", True)
print(len(a))
print(len(b))
def a():
    if len(b) == 8:
        s = b[:-1]
        # fixed = b.append(d)
        print(f"se ejecuta {s}")
        # print(f"se ejecuta {}")
        
a()
