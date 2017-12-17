import webbrowser


def open_website(json_response):
    website_name = (json_response['result']['parameters']['web_name'])
    my_list = website_name.split('.')

    name = website_name.split('.')[0]
    if len(my_list) >= 2:
        domain = website_name.split('.')[1]
    else:
        domain = 'com'

    webbrowser.open('https://www.' + name + '.' + domain)
