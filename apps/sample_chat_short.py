import wave
import time
import pyaudio
import random

class play:

    def play(self, name):
        wf = wave.open(name, "rb")
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), 
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True)
        data = wf.getnframes()
        while data > 0:
            buf = wf.readframes(min(1024, data))
            stream.write(buf)
            data -= 1024
        stream.close()
        p.terminate()
        wf.close()

    def pattern1(self):
        time.sleep(5)
        self.play("sentence/2.wav")
        time.sleep(5)
        self.play("sentence/5.wav")
        time.sleep(5)
        self.play("sentence/8.wav")
        time.sleep(1)
        self.play("sentence/82.wav")
        time.sleep(7)
        self.play("sentence/903.wav")

    def pattern2(self):
        time.sleep(5)
        self.play("sentence/3.wav")
        time.sleep(5)
        self.play("sentence/6.wav")
        time.sleep(5)
        self.play("sentence/9.wav")
        time.sleep(7)
        self.play("sentence/904.wav")

    def pattern3(self):
        time.sleep(5)
        self.play("sentence/4.wav")
        time.sleep(5)
        self.play("sentence/7.wav")
        time.sleep(5)
        self.play("sentence/10.wav")
        time.sleep(7)
        self.play("sentence/905.wav")
        
def main():
    d = play()
    d.play("sentence/433.wav")
    d.play("sentence/901.wav")
    #time.sleep(1)
    d.play("sentence/902.wav")
    a = random.randint(1, 3)
    
    if a == 1:
      d.pattern1()
    elif a == 2:
      d.pattern2()
    else:
      d.pattern3()
    
    time.sleep(5)
    d.play("sentence/2.wav")
    d.play("sentence/712.wav")
    d.play("sentence/343.wav")
    time.sleep(1)
    d.play("sentence/73.wav")
    d.play("sentence/802.wav")
if __name__ == '__main__':
    main()
