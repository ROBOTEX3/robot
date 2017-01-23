from library import client
import time
import threading



def shoe_listener(request):
    x = request['x']
    y = request['y']
    state = request['state']
    if state == 'left-check':
        client.speak('left')
    elif state == 'right-check':
        client.speak('right')
    client.get_shoe(shoe_listener)

class MainThread(threading.Thread):
    def __init__(self):
       super(MainThread, self).__init__()
    def run(self):
        client.get_shoe(shoe_listener)

thread = MainThread()
client.startListener(thread)
