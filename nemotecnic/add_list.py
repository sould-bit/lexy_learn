#%%
from nemotecnic.world_english import get_random, word

def open_readlines(archivo, split = None):
    with open(archivo, "r") as  read:
        content = read.readlines()
        
        # if split == True:
        #     data  = content.split("*\n")
        # else:
        #     data = content
        return content


def open_read(archivo, split = None):
    with open(archivo,"r")as read:
        content = read.read()
        if split == True:
            data = content.split("*\n")
        else:
            data = content
        return data
    
    
def top_10():
    
        data_split  = open_read("top_10.txt",True)
        
        count_splits = len(data_split ) -  1
        print(
            f" ejecutando top_10 \n van {count_splits}")
        
        lista = []
        numbers_objects = ""
        defi = data_split[count_splits-1]
        
        lista.append(defi)
        numbers_objects = str("".join(lista))
        
        # if count_splits >= 8:
        #     return f"\n\n {randon_list(responses_motivation)}"
        
        porcentaje = len(data_split) / 8 *1000 // 10
        return f" {numbers_objects} \n\n alcansaste un {porcentaje} % "
        
    

def ciclo_top_10(lista):
    print(f"\n realizando el ciclo de top_10")
    if not hasattr(ciclo_top_10, 'indice_actual'):
        ciclo_top_10.indice_actual = 0
    
    elemento = lista[ciclo_top_10.indice_actual]
    ciclo_top_10.indice_actual = (ciclo_top_10.indice_actual + 1) % len(lista) 
    return elemento

# agregamos , los datos  si no estan repetidos
def add_word(add_word):
        
        content = open_readlines("top_10.txt")
        
        
        if add_word not in  content :
            content.append(add_word+"*\n")
            print(
                f"añadiendo {word} a los top_10 " )
            
            # archivo.close()
            
            with open("word_learn.txt","r")as read_word_list:
                content_word_list = read_word_list.readlines()
                content_word_list.append(add_word+"*\n")
                print(f"añadiendo {word} a la lista de palabras " )
                
            with open("word_learn.txt", "w")as list_words_learn:
                list_words_learn.writelines(content_word_list)
                list_words_learn.close()
            with open(
                "top_10.txt", 'w') as writing:
                writing.writelines(content)

                writing.close()
                return top_10()
 
        else:
            print("la palabra y definicion ya se encuentran  en el top_10 , se buscara otra :)",)
            return main()
        
        

   
def main ():
    a = get_random()
    readlines = open_readlines("top_10.txt", split= True)
    count_lines = len(readlines)
    if count_lines > 174 :
         read = open_read("top_10.txt", split= True)
         count_linesread = len(read)
        #  words = read.pop(-1)
         print(f"{count_linesread}")
         return ciclo_top_10(read)
    else :
        return add_word(a)

        
    
# a =get_random()
# add_word(a)    