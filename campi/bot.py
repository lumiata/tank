import json

import picamera
import subprocess

from core.bot import Bot

usage_str = """
#help# - Print commands
#capture# - Capture an image from the cam
"""


class CamPi(Bot):
    def __init__(self, channel_name):
        super(CamPi, self).__init__(["message"], channel_name)
        self.camera = picamera.PiCamera()
        self.setup()

    def usage(self):
        return usage_str

    def setup(self):
        self.add_command("^help$", self.help)
        self.add_command("^capture$", self.capture)

    def parser(self, message):
        data = json.loads(message)
        if "text" in data:
            text = data["text"]
            for command in self.commands:
                matched = command.match(text)
                if matched:
                    command.handler()
                    return

    def help(self):
        self.say(self.usage().replace("#", "`"))

    def capture(self):
        subprocess.Popen(["/usr/bin/omxplayer", "data/camera_capture_sound.mp3"])
        self.camera.capture("image.jpg")
        self.client.slacker.files.upload("image.jpg", filename="image.jpg", channels=self.channel_name)
