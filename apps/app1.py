from library import client
import time
import threading

class MainThread(threading.Thread):
    def __init__(self):
       super(MainThread, self).__init__()
    def run(self):
        client.speak('hello')

thread = MainThread()
client.startListener(thread)
