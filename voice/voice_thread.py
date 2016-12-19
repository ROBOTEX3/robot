import threading
import json

apps = [
    'app1',
    'app2'
]

automaton = [
    {
        'state': 0,
        'next': lambda x: 1 if x == 'switch' else 0
    },
    {
        'state': 1,
        'next': lambda x: 2 if x in apps else 1
    },
    {
        'state': 2,
        'next': lambda x: 1 if x == 'switch' else 0
    }
]

class VoiceThread(threading.Thread):
    def __init__(self, log, app, voice, changeApp):
        super(VoiceThread, self).__init__()
        self.log = log
        self.app = app
        self.voice = voice
        self.changeApp = changeApp

    def run(self):
        automata = automaton[0]
        while True:
            response = self.voice.stdout.readline()
            self.log.communication('voice: receive ' + response)
            automata = automata['next'](response)
            state = automata['state']
            if state == 0:
                self.app.stdin.write(json.dumps({
                    "response": response,
                    "request": {"module": "voice"}
                }) + '\n')
            elif state == 2:
                self.app = self.changeApp(response + '.py')

