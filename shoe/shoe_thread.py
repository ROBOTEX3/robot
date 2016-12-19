import threading
import json

class ShoeThread(threading.Thread):
    def __init__(self, log, app, shoe):
        super(ShoeThread, self).__init__()
        self.log = log
        self.app = app
        self.shoe = shoe

    def run(self):
        while True:
            response = self.shoe.stdout.readline()
            self.log.communication('shoe: receive ' + response)
            try:
                self.app.stdin.write(json.dumps({
                    "response": json.loads(response),
                    "request": {"module": "shoe"}
                }) + '\n')
            except ValueError:
                break

    def changeApp(self, app):
        self.app = app
