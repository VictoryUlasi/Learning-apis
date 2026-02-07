#LLMs are cool :) made by Victory Ulasi

from ollama import chat, ChatResponse
import os
import requests
import json

os.system('cls')
boot_up = True

def get_user_info(): #Runs on initial boot up
    url = 'http://ip-api.com/json/'
    user_info = json.dumps(requests.get(url).json() , indent=None)
    
    with open('granite_memory.txt', 'w') as granite_memory: #Redo Entire Function tmr********************************************************
            injection = 'Answer in under 20 words'
            setup = f'''Follow these instructions: {injection}
                        I am located here: {user_info}'''
            granite_memory.write(setup)

def ai(query , memory): # "Brains" behind the model
    
    response: ChatResponse = chat(model='granite4:1b', messages=[
        
        {
            'role': 'user',
            'content': f'''This is our conversation up until now: {memory}
                            This is my question: {query}''',
        }
    
    ])
    return response.message.content
    
while True:
    #On first run this will excecute, can probably remove just redundant TBH
    if (boot_up):
        get_user_info()
        boot_up = False
    
    #Subsequent Runs start from here
    memory = str()
    query = input("Query: ")
    
    with open('granite_memory.txt' , 'r') as granite_memory: #opens memory file and stores entire file in variable before passing to ai function
        memory = granite_memory.read()
    
    response = ai(query , memory)
    os.system('cls')
    
    with open('granite_memory.txt', 'a') as granite_memory:
        granite_memory.write(f'My question -- {query}\n')
        granite_memory.write(f'Your response -- {response}\n')
    
    print(query)
    print(f'::{response}')
    
    
    
    

