from message.manejador_mensajes import responses_motivation,randon_list



def remove_top(name):
    list = "top_10.txt"
    
    def remove(list):
        with open(list, "w") as file:
            file.write("")
    
    remove(list)
    messaje=randon_list(responses_motivation)
    welcome = f"hi {name},come on Br@ let's start again \n\n{messaje} "
    
    return  welcome
        



