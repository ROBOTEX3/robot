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
            client.right(int(30 * x))
            time.sleep(2)
            client.move_acc(int(face['distance']))
        else:
            client.left(int(-30 * x))
            time.sleep(2)
            client.move_acc(int(face['distance']))
    client.get_face_positions(camera_listener)

class MainThread(threading.Thread):
    def __init__(self):
       super(MainThread, self).__init__()
    def run(self):
        client.get_face_positions(camera_listener)

thread = MainThread()
client.startListener(thread)
