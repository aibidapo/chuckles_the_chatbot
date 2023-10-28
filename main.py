import openai
from dotenv import dotenv_values
from fastapi import FastAPI, Form
from typing import Annotated

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


app = FastAPI()

chat_log = [{
    'role': 'system',
    'content': 'You are a Python tutor AI, completely dedicated to teaching users how to learn Python programming from scratch. please provide clear instructions\
        on Python concepts, best practices and syntax. Help create a path of learning for users to be able to create "real life, production-ready python applications".'
}]

@app.post("/")
async def chat(user_input: Annotated[str, Form()]):
        
    chat_log.append({'role': 'user', 'content': user_input})
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = chat_log,
        
        temperature = 0.7
    )
    
    bot_reponse = response['choices'][0]['message']['content']
    chat_log.append({'role': 'assistant', 'content': bot_reponse})

    return bot_reponse