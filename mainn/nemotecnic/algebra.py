#%%
import random

def Notas_nemotecnics():
    ejemplo = 3
    algebra = [
        ('Propiedad Refelxiva',' TEXTO1'),
        ('Propiedad Simetrica', 'texto2'),
        ('Propiedad distributiva', 'texto3')
            ]
    
    random_tupla = random.choice(algebra)
    notaa = f"{random_tupla[0]}: {random_tupla[1]}:{random_tupla[2]}"
    return notaa
Notas_nemotecnics()

