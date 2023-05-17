#%%
# from world_english import get_random
from nemotecnic.funtions import open_write, open_read, open_readlines, ciclo_top_10
from nemotecnic.world_english import get_random

import os 



# retornamos la palabra 
def tops():
        data_split  = open_read(name_arch,True)
        
        count_splits = len(data_split ) -  1
        print(
            f" ejecutando top_10 \n van {count_splits}")
        
        lista = []
        numbers_objects = ""
        defi = data_split[count_splits-1]
        
        lista.append(defi)
        numbers_objects = str("".join(lista))
        
       
        
        porcentaje = len(data_split) / 8 *1000 // 10
        return f" {numbers_objects} \n\n alcansaste un {porcentaje} % "
    
    
    
    
    



def main (user_top):
    # si el usuario ya tiene  archivo
    # name_arch = os.path.splitext(user_top)[0]
    global name_arch
    name_arch  = user_top + ".txt"
    if os.path.isfile(name_arch):
        data = open_readlines(name_arch)
        # antes de agregar los datos , nesesitamos validar si ya tiene mas de 7 words 
        count_words =len(data)
        print("leido")
        if count_words > 174:
            read = open_read(name_arch,split=True)
            ciclo_top_10(read)
            
            # iteramos sobre la lista de palabras 
            
        else: 
            word = get_random()
            # validamos si la palabra esta en el archivo 
            if word not in data:
                
                data.append(word+"*\n")
            
                user_register = user_top + "_register.txt"
                
                data_register = open_readlines(user_register)
                content_register = data_register.append(word+"*\n")
                #añadimos la data  a los tops
                print(f"añadiendo la data al top de {user_top}")
                open_write(user_top, data, True)
                # añadimos la data a los register 
                print(f"añadiendo la data al Register de {user_top}")
                # open_write(user_register, content_register, readline= True)
                return tops()
                
    
                
                # open_write(name_arch, "", True, content)
                # open_write(name_arch, "register", True, content)
                
            # añadimos la palabra 
            

    else:
        # creamos un archivo para el usuario
        
        print("creando")
        open_write(user_top )
        
        response = f"welcome {user_top} \n\n\n,come on press again ;)"
        return response
        

# if __name__ = "__main__":

