from library import client
import time
import threading

status = {'stage': 'search'}

def distant_listener(request):
    right = request['right']
    left = request['left']
    if status['stage'] == 'search':
        if right < 100 or left < 100:
            if right != left:
                if right > left:
                    client.move(int(left), 100)
                else:
                    client.move(100, int(right))
            else:
                client.move(100, 80)
        else:
            client.move(100, 100)
    if status['stage'] == 'search':
        client.get_distant(distant_listener)

def camera_listener(request):
    if len(request['faces']) > 0:
        if status['stage'] == 'search':
            client.speak('found')
            status['stage'] = 'found'
        elif status['stage'] == 'found':
            face = request['faces'][0]
            x = face['x']
            if x < 0.1 and x > -0.1:
                client.stop()
                status['stage'] = 'reach'
                client.speak('finished')
            else:
                if x > 0:
                    client.move(int(30 * x), 0)
                else:
                    client.move(0, int(-30 * x))
    if status['stage'] != 'reach':
        client.get_face_positions(camera_listener)

class MainThread(threading.Thread):
    def __init__(self):
       super(MainThread, self).__init__()
    def run(self):
        client.get_face_positions(camera_listener)
        client.get_distant(distant_listener)

thread = MainThread()
client.startListener(thread)
