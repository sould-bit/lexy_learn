import pandas as pd 
import os 

def open_readlines(archivo:str):
    with open(archivo, "r") as  read:
        data  = read.readlines()
        read.close()
        return data
    
def open_read(archivo, split = None):
    print("open read")
    with open(
        archivo,"r")as read:
        content = read.read()
        if split == True:
            data = content.split("*")
            read.close()
        else:
            data = content
            read.close()
        return data
    
def open_write(archivo
               , date= None, readline=None):
     print("open write")
     with open(
                f"{archivo}.txt", 'w') as writing:
                if date == None:
                    writing.write("")
                    writing.close()
                elif readline == True:
                    writing.writelines(date)
                    writing.close()
            
                else:
                    writing.write(date)
                    writing.close()
    #  if os.path.isfile(f"{archivo}_register.txt"):
         
    #      writing.writelines(f"{date}")
    #  else:
     with open(f"{archivo}_register.txt", 'w')as register:
                if date == None:
                    register.write("")
                    register.close()
                elif readline == True:
                    register.writelines(date)
                    register.close()
                else:
                    register.write(date)
                    register.close()
         

def open_add(archivo, dato):
    with open(archivo,"a")as read:
        read.write(dato)
        read.close()
        
    
def append_date(archivo, date, resgister = None):
    if os.path.isfile(archivo):
        open_add(archivo,date)
    elif resgister == True:
        open_write(f"{archivo}_register",date)
        
        
    else:
         open_write(archivo,date)


def ciclo_top_10(lista):
    print(f"\n realizando el ciclo de top_10")
    if not hasattr(ciclo_top_10, 'indice_actual'):
        ciclo_top_10.indice_actual = 0
    
    elemento = lista[ciclo_top_10.indice_actual]
    ciclo_top_10.indice_actual = (ciclo_top_10.indice_actual + 1) % len(lista) 
    return elemento