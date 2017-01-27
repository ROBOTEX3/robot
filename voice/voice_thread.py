import threading
import json

apps = [
    'app1',
    'app2'
]

automaton = [
    {
        'state': 0,
        'next': lambda x: 1 if x == 'switch' else 3 if x == 'exit' else 0
    },
    {
        'state': 1,
        'next': lambda x: 2 if x in apps else 1
    },
    {
        'state': 2,
        'next': lambda x: 1 if x == 'switch' else 0
    },
    {
        'state': 3,
        'next': lambda x: True
    }
]

class VoiceThread(threading.Thread):
    def __init__(self, log, app, voice, changeApp, exitCore):
        super(VoiceThread, self).__init__()
        self.log = log
        self.app = app
        self.voice = voice
        self.changeApp = changeApp
        self.exitCore = exitCore

    def run(self):
        automata = automaton[0]
        while True:
            response = self.voice.stdout.readline()
            if response == '':
                continue
            response = response.replace('\n', '')
            self.log.communication('voice: receive ' + response)
            if response == 'cancel':
                automata = automaton[0]
                continue
            automata = automaton[automata['next'](response)]
            state = automata['state']
            print state
            if state == 0:
                self.app.stdin.write(json.dumps({
                    "response": response,
                    "request": {"module": "voice"}
                }) + '\n')
            elif state == 2:
                self.app.terminate()
                self.app = self.changeApp(response + '.py')
            elif state == 3:
                self.exitCore()

