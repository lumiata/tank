from core.commands import Command
from slack.client import Client


class Bot(object):
    def __init__(self, stream_filters, channel_name):
        self.client = Client(filters=stream_filters)
        self.commands = []
        self.channel_name = channel_name

    def usage(self):
        raise NotImplementedError()

    def parser(self, message):
        raise NotImplementedError()

    def setup(self):
        raise NotImplementedError()

    def add_command(self, pattern, handler):
        self.commands.append(Command(pattern, handler))

    def say(self, message):
        response = self.client.send(message, channel=self.channel_name)

    def run(self):
        self.client.run(self.parser)

