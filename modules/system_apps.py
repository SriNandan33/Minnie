import os


from .import textToSpeech

list_of_apps = {
    '3D Builder': 'com.microsoft.builder3d:',
    'Action Center':   'ms-actioncenter:',
    'Clock': ' ms-clock:',
    'Calculator':  'calculator:',
    'Calendar':    'outlookcal:',
    'Camera':  'microsoft.windows.camera:',
    'Candy Crush Soda Saga':   'candycrushsodasaga:',
    'Connect': 'ms-projection:',
    'Cortana': 'ms-cortana:',
    'Drawboard PDF':   'drawboardpdf:',
    'Facebook':    'fb:',
    'Feedback Hub':   'feedback-hub:',
    'Get Help':    'ms-contact-support:',
    'Music':    'mswindowsmusic:',
    'Mail':    'outlookmail:',
    'Maps':    'bingmaps:',
    'Microsoft Edge': ' microsoft-edge:',
    'Movies': 'mswindowsvideo:',
    'News':    'bingnews:',
    'OneNote': 'onenote:',
    'Paint':    'ms-paint:',
    'People':  'ms-people:',
    'Settings':    'ms-settings:',
    'Skype':   'ms-projection:',
    'Store':   'ms-windows-store:',
    'Tips':    'ms-get-started:',
    'Twitter': 'twitter:',
    'Voice Recorder':  'ms-callrecording:',
    'Weather': 'bingweather:',
    'Xbox':    'xbox:',
}


def open_app(json_response):
    app_name = (json_response['result']['parameters']['app_name'])
    app_name = app_name.title()
    if app_name in list_of_apps.keys():
        os.system('start {0}'.format(list_of_apps[app_name]))
    else:
        print('Sorry, I can not open {0}'.format(app_name))
        textToSpeech.speakout('Sorry, I can not open {0}'.format(app_name))