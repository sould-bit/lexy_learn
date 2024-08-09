
import ollama

def response_ollama(text):
    message =[
        {
            'role':'user',
            'content': f'{text}'
        }
    ]


    response = ollama.chat(model='asisten_V0:latest',messages=message)

    
    
    print(response['message']['content'])
    return response['message']['content'] 


