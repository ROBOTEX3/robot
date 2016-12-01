from library import client
import time
import threading

def distant_listener(request):
    right = request['right']
    left = request['left']
    if right < 100 or left < 100:
        if right != left:
            if right / left > 2:
                turn = -(100 - left) / 5
            elif left / right > 2:
                turn = (100 - right) / 5
            else:
                turn = (right - left) * (200 - right - left) / 10
            client.move(int(100 + turn), int(100 - turn))
        else:
            client.move(100, 80)
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
