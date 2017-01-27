from library import client
import time
import threading

def camera_listener(request):
    keys = request['faces'].keys()
    if len(keys) > 0:
        face = request['faces'][keys[0]]
        if face['name'] == '':
            client.speak('"I dont know you"')
        else:
            client.speak(face['name'])
        x = face['x']
        if x > 0:
            client.move(int(300 * x), 0)
        else:
            client.move(0, int(-300 * x))
            time.sleep(0.1)
            client.stop()
    client.get_face_positions(camera_listener)

class MainThread(threading.Thread):
    def __init__(self):
       super(MainThread, self).__init__()
    def run(self):
        client.get_face_positions(camera_listener)

thread = MainThread()
client.startListener(thread)
