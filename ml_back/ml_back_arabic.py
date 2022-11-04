from ml_back.gpt_3 import generate_text

def generate_email(tone, key_points):
    translate_key_points_to_arabic = generate_text(
        """Translate this Arabic sentence to English : {key_points} """.format(key_points=key_points), max_tokens=200)
    english_email = generate_text(
        """Write {tone} email about: {translate_key_points_to_arabic} """.format(tone=tone, translate_key_points_to_arabic=translate_key_points_to_arabic), max_tokens=200)
    arabic_email = translate_key_points_to_arabic = generate_text(
        """Translate this email to Arabic: {english_email} """.format(english_email=english_email), max_tokens=300, temperature=0)
    return arabic_email


def generate_sms(tone, context):
    translate_context_to_arabic = generate_text(
        """Translate this Arabic sentence to English : {context} """.format(context=context), max_tokens=200)
    english_sms = generate_text(
        """Write {tone} sms about: {translate_context_to_arabic} """.format(tone=tone, translate_context_to_arabic=translate_context_to_arabic), max_tokens=200)
    arabic_sms = translate_key_points_to_arabic = generate_text(
        """Translate this SMS to Arabic: {english_sms}. """.format(english_sms=english_sms), max_tokens=300, temperature=0)
    return arabic_sms