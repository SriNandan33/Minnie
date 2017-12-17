from intent_resolver import get_json_response
from task_picker import TaskIdentifier

user_input = input()
json_response = get_json_response(user_input)
speech_response = (json_response['result']['fulfillment']['speech'])
print(speech_response)
output_intent = (json_response['result']['metadata']['intentName'])

if output_intent:
    getattr(TaskIdentifier, output_intent)(json_response)
