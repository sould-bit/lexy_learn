#%%
import pandas as pd 
from AyDictionary import AyDictionary
from translate import Translator
from nltk.corpus import cmudict



def get_random():
    df = pd.read_csv('20k.txt', header= None,   names=['word'])
    # seleccionamos aleatoriamente una palabra del data frame
    word = df.sample()['word'].values[0]
    #obtener la definicion de la palabra 
    dictionary = AyDictionary(word)
    print(f"Buscando definicion para , {word}")
    dict = dictionary.getMeanings()
    if word in dict and dict[word]:
        print("definicion  encontrada ", dict)
        # print(type(dict))
    elif word  in  dict and dict[word] == None:
        df.drop(df[df['word']== word].index, inplace= True)
        print(f"se eliminara {word}")
        df.to_csv("20k.txt", index=False, )
        # return get_random()
    
    #traduccion con traslate
    print("traducciendo ", word )
    
    traductor_traslate = Translator(to_lang="es")
    
    traslation = traductor_traslate.translate(word)
    
    print("traduccion encontrada es", traslation)
        
    #obtener la trasnquipcion fonetica 
    fonetic = cmudict.dict()
    if word in fonetic:
            phonetic = fonetic[word]
            print("se encontro la  fonetica")
    else:
        print(f'la fonetica de {word} no se encontro')
        phonetic = "Unknow"
    

    
    # devuelve la palabra , traduccion y fonetica 
    return {'word': word , 'form': dict,"traslation":traslation, 'phonetic': phonetic}


if __name__ == "__main__":
     random_word = get_random()
    #  print("word", random_word['word'],"translation", random_word['traslation'],"fonetica", random_word['phonetic'])
     print(random_word)
