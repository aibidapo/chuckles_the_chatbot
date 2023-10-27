import openai

from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config["OPENAI_API_KEY"]


response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [{
        'role': 'system',
        'content': 'You are a helpful assistant'
    }]
)

print(response)