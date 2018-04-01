import pyttsx
import speech_recognition


from intent_resolver import get_json_response
from task_picker import TaskIdentifier

# Setup for Speech Recognition
recognizer = speech_recognition.Recognizer()  # Speech Recognizer

# Setup for Text-To-Speech
voiceEngine = pyttsx.init()  # Text to Speech Engine
voiceEngine.setProperty('rate', 150)  # sets word frequency
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
voiceEngine.setProperty('voice', voice_id)  # sets voice to female voice


def listen():
    ''' Listen through microphone and recognizes with GSR'''
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Waiting for your command")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

if __name__ == '__main__':
    print('listening....')
    while True:

        try:
            # user_input = listen()
            user_input = input()
            json_response = get_json_response(user_input)
            speech_response = (json_response['result']['fulfillment']['speech'])
            voiceEngine.say(speech_response)
            voiceEngine.runAndWait()
            output_intent = (json_response['result']['metadata']['intentName'])
            if output_intent:
                getattr(TaskIdentifier, output_intent)(json_response)

        except:
            pass
