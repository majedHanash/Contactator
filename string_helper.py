
def to_html_string(string):
    string = string.strip()
    string = string.replace('\n', '</br>')
    return string
def handle_dict_new_line(dictionary):
    return {key:handle_new_line(value) for (key,value) in dictionary.items()}

def handle_new_line(string):
    return string.replace('\r','').replace('\n','\\n')
