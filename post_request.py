from urllib import request
from ml_back import ml_back


def handle_post_request(request):
    use_case = request.form['useCase']

    if use_case == 'Email':
        return handle_email_request(request), build_email_data(request)
    elif use_case == 'SMS':
        return handle_sms_request(request), build_sms_data(request)
    elif use_case == 'Song':
        return handle_song_request(request), build_song_data(request)
    elif use_case == 'Story':
        return handle_story_request(request), build_story_data(request)
    elif use_case == 'Facebook':
        return handle_facebook_request(request), build_facebook_data(request)
    elif use_case == 'CoverLetter':
        return handle_cover_letter_request(request), build_cover_letter_data(request)
    elif use_case == 'VideoChannelDescription':
        return handle_video_channel_description_request(request), build_video_channel_description_data(request)
    elif use_case == 'BlogIdea':
        return handle_blog_idea_request(request), build_blog_idea_data(request)
    elif use_case == 'InterviewQuestions':
        return handle_interview_questions_request(request), build_interview_questions_data(request)
    elif use_case == 'JobDescription':
        return handle_job_description_request(request), build_job_description_data(request)
    elif use_case == 'Tagline':
        return handle_tagline_request(request), build_tagline_data(request)
    elif use_case == 'Testimonial':
        return handle_testimonial_request(request), build_testimonial_data(request)
    elif use_case == 'QuestionAnswer':
        return handle_question_answer_request(request), build_question_answer_data(request)
    elif use_case == 'KeywordsGenerator':
        return handle_keywords_generator_request(request), build_keywords_generator_data(request)
    elif use_case == 'BusinessIdeas':
        return handle_business_ideas_request(request), build_business_ideas_data(request)
    elif use_case == 'PostIdea':
        return handle_post_idea_request(request), build_post_idea_data(request)
    elif use_case == 'SEOMetaTitle':
        return handle_seo_meta_title_request(request), build_seo_meta_title_data(request)
    elif use_case == 'ProductDescription':
        return handle_product_description_request(request), build_product_description_data(request)


def handle_basic_data(request):
    data = dict()
    data['tone'] = request.form['tone']
    data['useCase'] = request.form['useCase']
    data['language'] = request.form['language']
    return data


def handle_email_request(request):

    return ml_back.generate_email(request.form['language'], request.form['tone'], request.form['keyPoints'])


def build_email_data(request):
    data = handle_basic_data(request)
    data['keyPoints'] = request.form['keyPoints']
    return data


def handle_sms_request(request):

    return ml_back.generate_sms(request.form['language'], request.form['tone'], request.form['context'])


def build_sms_data(request):
    data = handle_basic_data(request)
    data['context'] = request.form['context']
    return data


def handle_song_request(request):

    return ml_back.generate_song(request.form['language'], request.form['tone'], request.form['idea'])


def build_song_data(request):
    data = handle_basic_data(request)
    data['idea'] = request.form['idea']
    return data


def handle_story_request(request):

    return ml_back.generate_story(request.form['language'], request.form['tone'], request.form['idea'])


def build_story_data(request):
    data = handle_basic_data(request)
    data['idea'] = request.form['idea']
    return data


def handle_facebook_request(request):

    return ml_back.generate_facebook_ad(request.form['language'], request.form['tone'], request.form['productName'], request.form['productDescription'])


def build_facebook_data(request):
    data = handle_basic_data(request)
    data['productName'] = request.form['productName']
    data['productDescription'] = request.form['productDescription']
    return data


def handle_cover_letter_request(request):

    return ml_back.generate_cover_letter(request.form['language'], request.form['tone'], request.form['jobRole'], request.form['jobSkills'])


def build_cover_letter_data(request):
    data = handle_basic_data(request)
    data['jobRole'] = request.form['jobRole']
    data['jobSkills'] = request.form['jobSkills']
    return data


def handle_video_channel_description_request(request):

    return ml_back.generate_video_channel_description(request.form['language'], request.form['tone'], request.form['category'], request.form['name'], request.form['cover'])


def build_video_channel_description_data(request):
    data = handle_basic_data(request)
    data['category'] = request.form['category']
    data['name'] = request.form['name']
    data['cover'] = request.form['cover']
    return data


def handle_blog_idea_request(request):

    return ml_back.generate_blog_idea(request.form['language'], request.form['tone'], request.form['primaryKeyword'])


def build_blog_idea_data(request):
    data = handle_basic_data(request)
    data['primaryKeyword'] = request.form['primaryKeyword']
    return data


def handle_interview_questions_request(request):

    return ml_back.generate_interview_questions(request.form['language'], request.form['tone'], request.form['intervieweeBio'], request.form['interviewContext'])


def build_interview_questions_data(request):
    data = handle_basic_data(request)
    data['intervieweeBio'] = request.form['intervieweeBio']
    data['interviewContext'] = request.form['interviewContext']
    return data


def handle_job_description_request(request):

    return ml_back.generate_job_description(request.form['language'], request.form['tone'], request.form['role'])


def build_job_description_data(request):
    data = handle_basic_data(request)
    data['role'] = request.form['role']
    return data


def handle_tagline_request(request):

    return ml_back.generate_tagline(request.form['language'], request.form['tone'], request.form['description'])


def build_tagline_data(request):
    data = handle_basic_data(request)
    data['description'] = request.form['description']
    return data


def handle_testimonial_request(request):

    return ml_back.generate_testimonial(request.form['language'], request.form['tone'], request.form['name'], request.form['reviewTitle'])


def build_testimonial_data(request):
    data = handle_basic_data(request)
    data['name'] = request.form['name']
    data['reviewTitle'] = request.form['reviewTitle']
    return data


def handle_question_answer_request(request):

    return ml_back.generate_question_answer(request.form['language'], request.form['tone'], request.form['description'])


def build_question_answer_data(request):
    data = handle_basic_data(request)
    data['description'] = request.form['description']
    return data


def handle_keywords_generator_request(request):

    return ml_back.generate_keywords_generator(request.form['language'], request.form['tone'], request.form['primaryKeyword'])


def build_keywords_generator_data(request):
    data = handle_basic_data(request)
    data['primaryKeyword'] = request.form['primaryKeyword']
    return data


def handle_business_ideas_request(request):
    
    return ml_back.generate_business_ideas(request.form['language'], request.form['tone'], request.form['interest'], request.form['skills'])


def build_business_ideas_data(request):
    data = handle_basic_data(request)
    data['interest'] = request.form['interest']
    data['skills'] = request.form['skills']
    return data


def handle_post_idea_request(request):
    
    return ml_back.generate_post_idea(request.form['language'], request.form['tone'], request.form['topic'])


def build_post_idea_data(request):
    data = handle_basic_data(request)
    data['topic'] = request.form['topic']
    return data


def handle_seo_meta_title_request(request):
    
    return ml_back.generate_seo_meta_title(request.form['language'], request.form['tone'], request.form['keywords'])


def build_seo_meta_title_data(request):
    data = handle_basic_data(request)
    data['keywords'] = request.form['keywords']
    return data


def handle_product_description_request(request):
    
    return ml_back.generate_product_description(request.form['language'], request.form['tone'], request.form['name'], request.form['about'])


def build_product_description_data(request):
    data = handle_basic_data(request)
    data['name'] = request.form['name']
    data['about'] = request.form['about']
    return data
