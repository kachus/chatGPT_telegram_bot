
from lexicon.lexicon_ru import LEXICON_RU
from lexicon.prompts import PROMPTS
from environs import Env
import openai
import os
import dotenv
import random

dotenv.load_dotenv()


def askGPT(text: str) -> str:
    openai.api_key = os.getenv('API_TOKEN')
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature=0.6,
        max_tokens = 600,

    )
    return response.choices[0].text

def get_advice() -> str:
    request = PROMPTS['get_advice']
    return askGPT(request)


def get_prediction() -> str:
    request = random.choice(PROMPTS['predictions'])
    return askGPT(request)

