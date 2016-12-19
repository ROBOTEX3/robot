import threading
import json

class CameraThread(threading.Thread):
    def __init__(self, request, log, app, camera):
        super(CameraThread, self).__init__()
        self.request = request
        self.log = log
        self.app = app
        self.camera = camera

    def run(self):
        cmd = self.request['command']
        self.log.communication('camera: send ' + cmd)
        if cmd == 'face_positions':
            self.camera.stdin.write(cmd + '\n')
            response = self.camera.stdout.readline()
        self.log.communication('camera: receive ' + response)
        response = json.loads(response)
        self.app.stdin.write(json.dumps({"response":response, 'request':self.request}) + '\n')

    def changeApp(self, app):
        self.app = app
