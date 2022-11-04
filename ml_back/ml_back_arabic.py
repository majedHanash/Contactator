from ml_back.gpt_3 import generate_text

def generate_email(tone, key_points):
    english_translated_key_points = generate_text(
        """Translate this Arabic sentence to English : {key_points} """.format(key_points=key_points), max_tokens=200)
    english_email = generate_text(
        """Write {tone} email about: {english_translated_key_points} """.format(tone=tone, english_translated_key_points=english_translated_key_points), max_tokens=200)
    arabic_email = generate_text(
        """Translate this email to Arabic: {english_email} """.format(english_email=english_email), max_tokens=300, temperature=0)
    return arabic_email


def generate_sms(tone, context):
    english_translated_context = generate_text(
        """Translate this Arabic sentence to English : {context} """.format(context=context), max_tokens=200)
    english_sms = generate_text(
        """Write {tone} sms about: {english_translated_context} """.format(tone=tone, english_translated_context=english_translated_context), max_tokens=200)
    arabic_sms = generate_text(
        """Translate this SMS to Arabic: {english_sms}. """.format(english_sms=english_sms), max_tokens=300, temperature=0)
    return arabic_sms

def generate_story(tone, idea):
    english_translated_idea = generate_text(
        """Translate this Arabic sentence to English : {idea} """.format(idea=idea), max_tokens=200)
    english_story = generate_text(
        """Write me {tone} story plot about {english_translated_idea} """.format(tone=tone, english_translated_idea=english_translated_idea), max_tokens=200)
    arabic_story = translate_key_points_to_arabic = generate_text(
        """Translate this story to Arabic: {english_story}. """.format(english_story=english_story), max_tokens=300, temperature=0)
    return arabic_story