from library import client
import time
import threading



def shoe_listener(request):
    x = request['x']
    y = request['y']
    state = request['state']
    speed = x
    if y < 0:
        client.move(int(speed * (255 + y) / 255), int(speed))
    else:
        client.move(int(speed), int(speed * y / 255))
    client.get_shoe(shoe_listener)

class MainThread(threading.Thread):
    def __init__(self):
       super(MainThread, self).__init__()
    def run(self):
        client.get_shoe(shoe_listener)

thread = MainThread()
client.startListener(thread)
