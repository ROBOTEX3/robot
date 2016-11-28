import threading
import json

class DistantThread(threading.Thread):
    def __init__(self, request, log, app, distant):
        super(DistantThread, self).__init__()
        self.request = request
        self.log = log
        self.app = app
        self.distant = distant

    def run(self):
        cmd = self.request['command']
        self.log.communication('distant: send ' + cmd)
        if cmd == 'check':
            self.distant.stdin.write(cmd + '\n')
            response = self.distant.stdout.readline()
        self.log.communication('distant: receive ' + response)
        print response
        response = json.loads(response)
        self.app.stdin.write(json.dumps({"response":response, 'request':self.request}) + '\n')
