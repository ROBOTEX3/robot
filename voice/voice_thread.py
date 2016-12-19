import threading
import json

class VoiceThread(threading.Thread):
    def __init__(self, log, app, voice):
        super(VoiceThread, self).__init__()
        self.log = log
        self.app = app
        self.voice = voice

    def run(self):
        while True:
            response = self.voice.stdout.readline()
            self.log.communication('voice: receive ' + response)
            self.app.stdin.write(json.dumps({
                "response": response,
                "request": {"module": "voice"}
            }) + '\n')


