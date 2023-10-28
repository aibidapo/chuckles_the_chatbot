import openai
from dotenv import dotenv_values
# from fastapi import FastAPI, Form, Request
# from typing import Annotated
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse


config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

chat_log = []

while True:
    
    user_input = input("Enter your your message: ")

    if user_input.lower() == "stop":
        break
        
    chat_log.append({'role': 'user', 'content': user_input})


    response = openai.ChatCompletion.create(
        
        model = 'gpt-3.5-turbo',
        messages = chat_log,        
        temperature = 0
        
    )

    bot_reponse = response['choices'][0]['message']['content']
    chat_log.append({'role': 'assistant', 'content': bot_reponse})    
    
    print(bot_reponse)