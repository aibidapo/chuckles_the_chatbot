import openai
from dotenv import dotenv_values
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

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