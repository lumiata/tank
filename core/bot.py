from core.commands import Command
from slack.client import Client
import signal


class Bot(object):
    def __init__(self, stream_filters, channel_name):
        self.client = Client(filters=stream_filters)
        self.commands = []
        self.channel_name = channel_name
        signal.signal(signal.SIGABRT, self.shutdown)
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)
        self.startup()

    def startup(self):
        self.say("Hello Lumi! I'm here to serve")

    def shutdown(self):
        self.say("Goodbye folks!")

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
        return response

    def run(self):
        self.client.run(self.parser)

