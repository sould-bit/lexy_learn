#%%
import pandas as pd 
from AyDictionary import AyDictionary
from pyphonetics import Soundex
from translate import Translator

df = pd.read_csv('20k.txt', header= None,   names=['word'])


def get_random():
    # seleccionamos aleatoriamente una palabra del data frame
    word = df.sample()['word'].values[0]
    
    #obtener la definicion de la palabra 
    dictionary = AyDictionary(word)
    print(f"Buscando definicion para , {word}")

    dict = dictionary.getMeanings()
    print("definicion  encontrada ", dict)
    
    #traduccion con traslate
    print("traducciendo ", word )
    
    traductor_traslate = Translator(to_lang="es")
    
    traslation = traductor_traslate.translate(word)
    
    print("traduccion encontrada es", traslation)
        
   
    
    #obtener la fonetica de la palabra 
    soundex = Soundex()
    print("Buscando fonetic para", word)
    phonetic = soundex.phonetics(word)
    print("fonetic  encontrada ", phonetic)
    # devuelve la palabra , traduccion y fonetica 
    return {'word': word , 'form': dict,"traslation":traslation, 'phonetic': phonetic}


if __name__ == "__main__":
     random_word = get_random()
    #  print("word", random_word['word'],"translation", random_word['traslation'],"fonetica", random_word['phonetic'])
     print(random_word)