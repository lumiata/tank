import re


class Command:

    def __init__(self, pattern, handler):
        self.text = pattern
        self.pattern = re.compile(pattern)
        self.handler = handler

    def match(self, data):
        return self.pattern.match(data)

    def __str__(self):
        return "Command:[ " + self.text + "]"

