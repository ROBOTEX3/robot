from library import client
import time
import threading

def distant_listener(request):
    right = request['right']
    left = request['left']
    if right < 100 or left < 100:
        if right != left:
            if right > left:
                client.move(int(left), 300)
            else:
                client.move(300, int(right))
        else:
            client.move(300,80)
    else:
        client.move(300, 300)
    client.get_distant(distant_listener)

class MainThread(threading.Thread):
    def __init__(self):
       super(MainThread, self).__init__()
    def run(self):
        client.get_distant(distant_listener)

thread = MainThread()
client.startListener(thread)
