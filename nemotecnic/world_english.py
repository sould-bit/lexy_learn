#%%
import requests
import time
import pandas as pd 
from AyDictionary import AyDictionary
from translate import Translator
from nltk.corpus import cmudict

space = "\n**************" *1
# los separadores que no queremos que se muestren en el output del cliente 
separadores = {":": ",", "{":"","}":"","[":"","]":""}

def get_random():
    global word
    df = pd.read_csv('20k.txt', header= None,   names=['word'])
    word = df.sample()['word'].values[0]
    
    # seleccionamos aleatoriamente una palabra del data frame
    
    #obtener la definicion de la palabra 
    dictionary = AyDictionary(word)
    
    print(f"Buscando definicion para , {word} ,"+ space)
    #obtenemos la definicion del diccionario 
    try:    
        response = requests.get(f'http://wordnetweb.princeton.edu/perl/webwn?s={word}')
        dicti = dictionary.getMeanings()

#  c    ondicionamos si se encuentra o no la palabra en el diccionario 
        if word in dicti and dicti[word]:
            # obtenemos los valores ,  del diccionario  lo pasamos por una lista y por un string 
            definition_str =  str(list(dicti.values())) 
            # remplazamos los separadores , para limpiar los datos , 
            definition_separater = definition_str.translate(str.maketrans(separadores))
            # separamos  por coma  convirtiendoo en una lista con varios valores
            definition_split = definition_separater.split(", ")
            definition_split2 = []
            # recorremos la lista 
            for definition in definition_split:

                definition_str = f"-- {definition}\n"
                #agregamos a una nueva lista , para que retornen todos los valores de la lista y no solo el ultimo
                definition_split2.append(definition_str)
                # unimos la lista  a un string
                all_definitions = "".join(definition_split2)
            print(f"{type(definition_split)}")


            print("definicion  encontrada " + str(space))
            # print(type(dict))
        # si no se encuentra la palabra , si el valor del dict es none 
        elif word  in  dicti and dicti[word] == None:
            # eliminamos , la palabra 
            df.drop(df[df['word']== word].index, inplace= True)
            print(f"se eliminara {word}"+ space)
            # actualizamos el archivo , sin la palabra
            df.to_csv("20k.txt", index=False, )
            # iteramos , para buscar una palabra nueva 
            return get_random()
            # return get_random()
    except requests.exceptions.ConnectionError:
        print(" se fue el wifi parce ")
        time.sleep(5)
        return get_random()
        
    #traduccion con traslate
    print("traducciendo ", word + space)
    
    traductor_traslate = Translator(to_lang="es")
    traslation = traductor_traslate.translate(word)
    traslation_definitions = traductor_traslate.translate(all_definitions)
    if "MYMEMORY WARNING" in traslation and traslation_definitions:
        traslation  = "la traduccion se funio"
        traslation_definitions = "la traduccion se funio"
    
        print("traduccion encontrada es", traslation)
            
        #obtener la trasnquipcion fonetica 
        fonetic = cmudict.dict()
        if word in fonetic:
                phonetic = fonetic[word]
                print("se encontro la  fonetica"+ space)
                phonetic = f"phonetic {' '.join(phonetic[0])}"
        else:
            print(f'la fonetica de {word} no se encontro'+ space)
            phonetic = "Unknow"
            
        # devuelve la palabra , traduccion y fonetica 
        
        palabra =f"word: {word}"
        #  = f"{dict(dict1.values())}"
        try:
            return f"{palabra}\n\n  {all_definitions}\n\n{traslation_definitions}\nTraslation:\n{traslation}\n  \n{phonetic}\n\n"
        except UnboundLocalError as error:
            print("error  de varialble local manejado ",error)
        
        #      definicion  = f"- {defincion}"
    else:
        #obtener la trasnquipcion fonetica 
        fonetic = cmudict.dict()
        if word in fonetic:
                phonetic = fonetic[word]
                print("se encontro la  fonetica"+ space)
                phonetic = f"phonetic {' '.join(phonetic[0])}"
        else:
            print(f'la fonetica de {word} no se encontro'+ space)
            phonetic = "Unknow"
            
        # devuelve la palabra , traduccion y fonetica 
        
        palabra =f"word: {word}"
        #  = f"{dict(dict1.values())}"
        try:
            return f"{palabra}\n\n  {all_definitions}\n\n{traslation_definitions}\nTraslation:\n{traslation}\n  \n{phonetic}\n\n"
        except UnboundLocalError as error:
            print("error  de varialble local manejado ",error)
        
    


# get_random()
# print(get_random)