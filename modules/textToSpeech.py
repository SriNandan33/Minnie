import pyttsx


def speakout(input_text):
    voiceEngine = pyttsx.init()

    voiceEngine.setProperty('rate', 150)
    # voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    # voiceEngine.setProperty('voice',voice_id)
    # # voiceEngine.say('Email the author if you have wrapped or are interested in wrapping another text-to-speech engine for use with pyttsx.')
    # voiceEngine.say('Prabhas is an Indian film actor best known for his work in Telugu cinema. Prabhas made his film debut with the 2002 drama film Eeswar. His works include Varsham, Chatrapathi, Chakram, Billa, Darling, Mr. Perfect, and Mirchi.')
    # voiceEngine.runAndWait()

    voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    voiceEngine.setProperty('voice', voice_id)
    # voiceEngine.say('Email the author if you have wrapped or are interested in wrapping another text-to-speech engine for use with pyttsx.')
    voiceEngine.say(input_text)
    voiceEngine.runAndWait()
