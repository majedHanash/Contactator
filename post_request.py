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
