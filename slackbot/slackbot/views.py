import json
import requests
from django.http import HttpResponse

SLACK_CHANNEL_URL = "https://hooks.slack.com/services/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"

USER_ID = 'UDNN9G11R'
BOT_ID = 'BDP1U1T9B'

def index(request):
    data = json.loads(request.body)
    print(data)

    if data['event'].get('bot_id') == BOT_ID:
        return HttpResponse()

    if data['event']['type'] == "app_mention":
        text = data['event']['text']
        print("Someone mentioned me! They said: " + text)
        requests.post(SLACK_CHANNEL_URL,
                      json={'text': "Someone mentioned me! They said: " + text},
                      headers={'Content-Type': 'application/json'})

    return HttpResponse()


def hello(request):
    requests.post(SLACK_CHANNEL_URL,
                  json={'text': "Hello, my friends!"},
                  headers={'Content-Type': 'application/json'})
    return HttpResponse("Done!")
