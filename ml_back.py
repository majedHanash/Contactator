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


def generate_cover_letter(tone, job_role, job_skills):
    return generate_text(
        """Write me {tone} cover letter for {job_role} role. skills: {job_skills} """.format(tone=tone, job_role=job_role, job_skills=job_skills), max_tokens=150)


def generate_video_channel_description(tone, category, name, cover):
    return generate_text(
        """Write me {tone} video channel description for {category} channel called {name}. We cover {cover}. """.format(tone=tone, category=category, name=name, cover=cover), max_tokens=100)


def generate_blog_idea(tone, primary_keyword):
    return generate_text(
        """suggest {tone} blog idea {primary_keyword}""".format(tone=tone, primary_keyword=primary_keyword), max_tokens=100)


def generate_interview_questions(tone, interviewee_bio, interview_context):
    return generate_text(
        """suggest {tone} interview questions for {interviewee_bio}. {interview_context}""".format(tone=tone, interviewee_bio=interviewee_bio, interview_context=interview_context), max_tokens=100)


def generate_job_description(tone, role):
    return generate_text(
        """write me {tone} job description for {role}""".format(tone=tone, role=role), max_tokens=200)


def generate_tagline(tone, description):
    return generate_text(
        """suggest {tone} tagline phrase for {description}""".format(tone=tone, description=description), max_tokens=25)


def generate_testimonial(tone, name, review_title):
    return generate_text(
        """suggest {tone} testimonial about {name}. {review_title}""".format(tone=tone, name=name, review_title=review_title), max_tokens=150)


def generate_question_answer(tone, description):
    return generate_text(
        """write {tone} questions about the following text: {description}""".format(tone=tone, description=description), max_tokens=100)


def generate_keywords_generator(tone, primary_keyword):
    return generate_text(
        """Generate {tone} related keywords to: {primary_keyword}""".format(tone=tone, primary_keyword=primary_keyword), max_tokens=100)


def generate_text(userPrompt, max_tokens=15):

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=userPrompt,
        temperature=0.79,
        max_tokens=max_tokens
    )
    return response.get("choices")[0]['text']
