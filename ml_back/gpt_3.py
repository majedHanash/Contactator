import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_text(userPrompt, max_tokens=15, temperature=0.76):
    
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=userPrompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.get("choices")[0]['text']
