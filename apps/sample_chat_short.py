import wave
import time
import pyaudio
import random
import pygame.mixer
from library import client
import threading

status = {
    'name': 'wait',
    'ready': False,
    'word': ''
}

class play:

    def play(self, name):
        wf = wave.open(name)
        pygame.mixer.init()
        pygame.mixer.music.load(name)
        pygame.mixer.music.play(-1)
        time.sleep(float(wf.getnframes()) / wf.getframerate())
        pygame.mixer.music.stop()

    #wf = wave.open(name, "rb")
       # p = pyaudio.PyAudio()
       # stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), 
        #    channels=wf.getnchannels(),
         #   rate=wf.getframerate(),
          #  output=True)
        #data = wf.getnframes()
        #while data > 0:
           # buf = wf.readframes(min(1024, data))
          #  stream.write(buf)
         #   data -= 1024
        #stream.close()
        #p.terminate()
        #wf.close()

    def pattern1(self):
        time.sleep(5)
        self.play("./apps/sentence/2.wav")
        time.sleep(5)
        self.play("./apps/sentence/5.wav")
        time.sleep(5)
        self.play("./apps/sentence/8.wav")
        time.sleep(1)
        self.play("./apps/sentence/82.wav")
        time.sleep(7)
        self.play("./apps/sentence/903.wav")

    def pattern2(self):
        time.sleep(5)
        self.play("./apps/sentence/3.wav")
        time.sleep(5)
        self.play("./apps/sentence/6.wav")
        time.sleep(5)
        self.play("./apps/sentence/9.wav")
        time.sleep(7)
        self.play("./apps/sentence/904.wav")

    def pattern3(self):
        time.sleep(5)
        self.play("./apps/sentence/4.wav")
        time.sleep(5)
        self.play("./apps/sentence/7.wav")
        time.sleep(5)
        self.play("./apps/sentence/10.wav")
        time.sleep(7)
        self.play("./apps/sentence/905.wav")

def voice_listener(word):
    if word in ('yes')
      status['word'] = word
    client.get_voice(voice_listener)

class MainThread(threading.Thread):
    d = play()
    d.play("./apps/sentence/433.wav")
    d.play("./apps/sentence/901.wav")
    #time.sleep(1)
    d.play("./apps/sentence/902.wav")
    a = random.randint(1, 3)
    
    if a == 1:
      d.pattern1()
    elif a == 2:
      d.pattern2()
    else:
      d.pattern3()
    
    time.sleep(5)
    d.play("./apps/sentence/2.wav")
    d.play("./apps/sentence/712.wav")
    d.play("./apps/sentence/343.wav")
    time.sleep(1)
    d.play("./apps/sentence/73.wav")
    d.play("./apps/sentence/802.wav")

if __name__ == '__main__':
    main()
    
