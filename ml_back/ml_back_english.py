
from ml_back.gpt_3 import generate_text


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
        """Write me {tone} cover letter for {job_role} role. skills: {job_skills} """.format(tone=tone, job_role=job_role, job_skills=job_skills), max_tokens=200)


def generate_video_channel_description(tone, category, name, cover):
    return generate_text(
        """Write me {tone} video channel description for {category} channel called {name}. We cover {cover}. """.format(tone=tone, category=category, name=name, cover=cover), max_tokens=100)


def generate_blog_idea(tone, primary_keyword):
    return generate_text(
        """suggest {tone} Blog idea with outline about {primary_keyword}.""".format(tone=tone, primary_keyword=primary_keyword), max_tokens=250)


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


def generate_business_ideas(tone, interest, skills):
    return generate_text(
        """Suggest {tone} business ideas for the field of {interest}. With skills: {skills}.""".format(tone=tone, interest=interest, skills=skills), max_tokens=150)


def generate_post_idea(tone, topic):
    return generate_text(
        """write {tone} (post/ caption) idea about topic: {topic}.""".format(tone=tone, topic=topic), max_tokens=150)


def generate_seo_meta_title(tone, keywords):
    return generate_text(
        """Generate {tone} SEO meta title for keywords: {keywords}.""".format(tone=tone, keywords=keywords), max_tokens=60)


def generate_product_description(tone, name, about):
    return generate_text(
        """Write {tone} product description for a product called: {name}. {about}""".format(tone=tone, name=name, about=about), max_tokens=200)

