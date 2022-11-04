from ml_back import ml_back_english, ml_back_arabic

def generate_email(language, tone, key_points):
    if language == "English":
        return ml_back_english.generate_email(tone, key_points)
    elif language == "Arabic":
        return ml_back_arabic.generate_email(tone, key_points)
    else: 
        return None

def generate_sms(language, tone, context):
    if language == "English":
        return ml_back_english.generate_sms(tone, context)
    elif language == "Arabic":
        return ml_back_arabic.generate_sms(tone, context)
    else:
        return None

def generate_song(language, tone, idea):
    if language == "English":
        return ml_back_english.generate_song(tone, idea)
    else:
        return None

def generate_story(language, tone, idea):
    if language == "English":
        return ml_back_english.generate_story(tone, idea)
    else:
        return ml_back_arabic.generate_story(tone, idea)

def generate_facebook_ad(language, tone, product_name, product_description):
    if language == "English":
        return ml_back_english.generate_facebook_ad(tone, product_name, product_description)
    else:
        return None

def generate_cover_letter(language, tone, job_role, job_skills):
    if language == "English":
        return ml_back_english.generate_cover_letter(tone, job_role, job_skills)
    else:
        return None

def generate_video_channel_description(language, tone, category, name, cover):
    if language == "English":
        return ml_back_english.generate_video_channel_description(tone, category, name, cover)
    else:
        return None

def generate_blog_idea(language, tone, primary_keyword):
    if language == "English":
        return ml_back_english.generate_blog_idea(tone, primary_keyword)
    else:
        return None

def generate_interview_questions(language, tone, interviewee_bio, interview_context):
    if language == "English":
        return ml_back_english.generate_interview_questions(tone, interviewee_bio, interview_context)
    else:
        return None

def generate_job_description(language, tone, role):
    if language == "English":
        return ml_back_english.generate_job_description(tone, role)
    else:
        return None

def generate_tagline(language, tone, description):
    if language == "English":
        return ml_back_english.generate_tagline(tone, description)
    else:
        return None

def generate_testimonial(language, tone, name, review_title):
    if language == "English":
        return ml_back_english.generate_testimonial(tone, name, review_title)
    else:
        return None

def generate_question_answer(language, tone, description):
    if language == "English":
        return ml_back_english.generate_question_answer(tone, description)
    else:
        return None

def generate_keywords_generator(language, tone, primary_keyword):
    if language == "English":
        return ml_back_english.generate_keywords_generator(tone, primary_keyword)
    else:
        return None

def generate_business_ideas(language, tone, interest, skills):
    if language == "English":
        return ml_back_english.generate_business_ideas(tone, interest, skills)
    else:
        return None

def generate_post_idea(language, tone, topic):
    if language == "English":
        return ml_back_english.generate_post_idea(tone, topic)
    else:
        return None

def generate_seo_meta_title(language, tone, keywords):
    if language == "English":
        return ml_back_english.generate_seo_meta_title(tone, keywords)
    else:
        return None

def generate_product_description(language, tone, name, about):
    if language == "English":
        return ml_back_english.generate_product_description(tone, name, about)
    else:
        return None

