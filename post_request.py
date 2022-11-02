from urllib import request
import ml_back


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


def handle_basic_data(request):
    data = dict()
    data['tone'] = request.form['tone']
    data['useCase'] = request.form['useCase']
    return data


def handle_email_request(request):

    return ml_back.generate_email(request.form['tone'], request.form['keyPoints'])


def build_email_data(request):
    data = handle_basic_data(request)
    data['keyPoints'] = request.form['keyPoints']
    return data


def handle_sms_request(request):

    return ml_back.generate_sms(request.form['tone'], request.form['context'])


def build_sms_data(request):
    data = handle_basic_data(request)
    data['context'] = request.form['context']
    return data


def handle_song_request(request):

    return ml_back.generate_song(request.form['tone'], request.form['idea'])


def build_song_data(request):
    data = handle_basic_data(request)
    data['idea'] = request.form['idea']
    return data


def handle_story_request(request):

    return ml_back.generate_story(request.form['tone'], request.form['idea'])


def build_story_data(request):
    data = handle_basic_data(request)
    data['idea'] = request.form['idea']
    return data


def handle_facebook_request(request):

    return ml_back.generate_facebook_ad(request.form['tone'], request.form['productName'], request.form['productDescription'])


def build_facebook_data(request):
    data = handle_basic_data(request)
    data['productName'] = request.form['productName']
    data['productDescription'] = request.form['productDescription']
    return data


def handle_cover_letter_request(request):

    return ml_back.generate_cover_letter(request.form['tone'], request.form['jobRole'], request.form['jobSkills'])


def build_cover_letter_data(request):
    data = handle_basic_data(request)
    data['jobRole'] = request.form['jobRole']
    data['jobSkills'] = request.form['jobSkills']
    return data


def handle_video_channel_description_request(request):

    return ml_back.generate_video_channel_description(request.form['tone'], request.form['category'], request.form['name'], request.form['cover'])


def build_video_channel_description_data(request):
    data = handle_basic_data(request)
    data['category'] = request.form['category']
    data['name'] = request.form['name']
    data['cover'] = request.form['cover']
    return data


def handle_blog_idea_request(request):

    return ml_back.generate_blog_idea(request.form['tone'], request.form['primaryKeyword'])


def build_blog_idea_data(request):
    data = handle_basic_data(request)
    data['primaryKeyword'] = request.form['primaryKeyword']
    return data


def handle_interview_questions_request(request):

    return ml_back.generate_interview_questions(request.form['tone'], request.form['intervieweeBio'], request.form['interviewContext'])


def build_interview_questions_data(request):
    data = handle_basic_data(request)
    data['intervieweeBio'] = request.form['intervieweeBio']
    data['interviewContext'] = request.form['interviewContext']
    return data


def handle_job_description_request(request):

    return ml_back.generate_job_description(request.form['tone'], request.form['role'])


def build_job_description_data(request):
    data = handle_basic_data(request)
    data['role'] = request.form['role']
    return data


def handle_tagline_request(request):

    return ml_back.generate_tagline(request.form['tone'], request.form['description'])


def build_tagline_data(request):
    data = handle_basic_data(request)
    data['description'] = request.form['description']
    return data
