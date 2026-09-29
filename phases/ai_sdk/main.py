from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


"""
this should be a factory for all the models and should be all the functions like sending a message and sending a strutured output message and sending a image, etc all of them 
"""


def openai_provider(model):
    openai = OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("BASE_URL"),
        model=model
    )
    return openai

def openai_chat(messages):
    openai = openai_provider("upstage/solar-pro4")
    response = openai.chat.completions(messages=messages)
    return response
    


