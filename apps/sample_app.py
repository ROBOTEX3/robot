from library import client
import time
import threading

def distant_listener(request):
    if request['right'] < 40 or request['left'] < 40:
        client.speak("stopping")
        client.stop()
    else:
        client.move(100, 100)
    client.get_distant(distant_listener)

def camera_listener(request):
    if len(request['faces']) > 0:
        client.speak('found')
    client.get_face_positions(camera_listener)


class MainThread(threading.Thread):
    def __init__(self):
       super(MainThread, self).__init__()
    def run(self):
        client.get_face_positions(camera_listener)
        client.get_distant(distant_listener)

thread = MainThread()
client.startListener(thread)
