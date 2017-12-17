import json
import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'd28c7b7f4dc140149ff4a3c66b8312ef'


def get_json_response(user_input):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()
    request.query = user_input
    response = request.getresponse()
    json_response = json.loads(response.read())

    return json_response
