import openai
from .env import key

openai.api_key = key

error_message = (
    "I'm sorry, there seems to be an internal error. Please try again later."
)


def text_response(data):
    try:
        response = openai.ChatCompletion.create(model="gpt-4", messages=data)
        return response["choices"][0]["message"]["content"]
    except openai.error.OpenAIError as e:
        if e.http_status == 500:
            return error_message
        else:
            return f"An error occurred: {e.message}"


def image_response(data):
    try:
        response = openai.Image.create(prompt=data, n=1, size="1024x1024")
        return response["data"][0]["url"]
    except openai.error.OpenAIError as e:
        if e.http_status == 500:
            return error_message
        else:
            return f"An error occurred: {e.message}"
