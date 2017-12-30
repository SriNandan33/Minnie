import speech_recognition


from intent_resolver import get_json_response
from task_picker import TaskIdentifier


recognizer = speech_recognition.Recognizer()


def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

if __name__ == '__main__':
    print('listening....')
    user_input = listen()
    json_response = get_json_response(user_input)
    speech_response = (json_response['result']['fulfillment']['speech'])
    print(speech_response)
    output_intent = (json_response['result']['metadata']['intentName'])

    if output_intent:
        getattr(TaskIdentifier, output_intent)(json_response)
