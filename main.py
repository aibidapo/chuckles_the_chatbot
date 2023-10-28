import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


chat_log = []

while True:
    
    user_input = input()
    if user_input.casefold() == 'stop':
        break
    
    chat_log.append({'role': 'user', 'content': user_input})
    
    

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = chat_log,
        
        temperature = 0.7
    )
    
    bot_reponse = response['choices'][0]['message']['content']
    chat_log.append({'role': 'assistant', 'content': bot_reponse})

    print(bot_reponse)