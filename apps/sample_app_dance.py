import time
from library import client
import threading 
import pygame.mixer

class MainThread(threading.Thread):
    def __init__(self):
          super(MainThread, self).__init__()
    def run(self):
        pattern = [0, 1, 0, 1]
        pygame.mixer.init(frequency=44100, size=-16, channels = 2, buffer=1024)
        sound = pygame.mixer.Sound("./sound/tempo_120.wave")    
        tempo = 120.0/120
    
        sound.play()
        for i in pattern:
            if i:
                client.right(30)
            else:
                client.left(30)
            time.sleep(tempo)    

        pygame.mixer.quit()
        client.speak('I am so tired')


thread = MainThread()
client.startListener(thread)
