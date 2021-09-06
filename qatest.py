import slack
import json
slack_token = 'your_bot_token'

with open('example.json', 'r') as json_file:
    parsed_json = json.load(json_file)
client = slack.WebClient(token=slack_token)
channels = parsed_json['channels']
for element in channels:
    channel = element['channel']
    text = element['text']
    client.chat_postMessage(channel=channel, text=text)
