import os

from slacker import Slacker
from slacksocket import SlackSocket


class Client:

    def __init__(self, filters):
        slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
        self.slacker = Slacker(slack_bot_token)
        self.socket = SlackSocket(slack_bot_token, event_filters=filters)

    def run(self, parser=None):
        for event in self.socket.events():
            parser(event.json)

    def send(self, message, channel):
        response = self.slacker.chat.post_message(channel=channel, text=message, as_user=True)
        return response
