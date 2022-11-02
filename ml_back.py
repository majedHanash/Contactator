import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_email(tone, key_points):
    return generate_text(
        """Write me {tone} email about {key_points} """.format(tone=tone, key_points=key_points), max_tokens=200)

def generate_sms(tone, context):
    return generate_text(
        """Write me {tone} sms about {context} """.format(tone=tone, context=context), max_tokens=40)

def generate_song(tone, idea):
    return generate_text(
        """Write me {tone} song lyrics about {idea} """.format(tone=tone, idea=idea), max_tokens=140)

def generate_story(tone, idea):
    return generate_text(
        """Write me {tone} story plot about {idea} """.format(tone=tone, idea=idea), max_tokens=200)

def generate_facebook_ad(tone, product_name, product_description):
    return generate_text(
        """Write me {tone} facebok ad about {product_name}. {product_description} """.format(tone=tone, product_name=product_name, product_description=product_description), max_tokens=150)




def generate_text(userPrompt, max_tokens=15):

    response = openai.Completion.create(
            model="text-davinci-002",
            prompt=userPrompt,
            temperature=0.79,
            max_tokens=max_tokens
            )
    return response.get("choices")[0]['text']

