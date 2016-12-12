from library import client
import time
import threading

def voice_listener(request):
    client.get_voice(voice_listener)

class MainThread(threading.Thread):
    def __init__(self):
       super(MainThread, self).__init__()
    def run(self):
        client.get_voice(voice_listener)

thread = MainThread()
client.startListener(thread)
