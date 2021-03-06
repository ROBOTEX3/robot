import wave
import time
import pyaudio
import random
import pygame.mixer

class play:

    def play(self, name):
        wf = wave.open(name)
        pygame.mixer.init()
        pygame.mixer.music.load(name)
        pygame.mixer.music.play(-1)
        time.sleep(float(wf.getnframes()) / wf.getframerate())
        pygame.mixer.music.stop()


        #wf = wave.open(name, "rb")
        #p = pyaudio.PyAudio()
        #stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), 
         #   channels=wf.getnchannels(),
          #  rate=wf.getframerate(),
           # output=True)
        #data = wf.getnframes()
        #while data > 0:
         #   buf = wf.readframes(min(1024, data))
         #   stream.write(buf)
         #   data -= 1024
        #stream.close()
        #p.terminate()
        #wf.close()
        
    def pattern21(self):
        time.sleep(2)
        self.play("./apps/sentence/21.wav")
        self.pattern31()
    def pattern22(self):
        time.sleep(2)
        self.play("./apps/sentence/22.wav")
        self.pattern32()
    def pattern23(self):
        time.sleep(2)
        self.play("./apps/sentence/231.wav")
        self.play("./apps/sentence/232.wav")
        a = random.randint(1, 2)
        if a == 1:
          self.pattern33()
        else:
          self.pattern34()
    def pattern24(self):
        time.sleep(2)
        self.play("./apps/sentence/24.wav")
        self.pattern57()
    def pattern25(self):
        time.sleep(2)
        self.play("./apps/sentence/25.wav")
        self.pattern809()
    def pattern31(self):
        time.sleep(1)
        self.play("./apps/sentence/31.wav")
        self.pattern41()
    def pattern32(self):
        self.play("./apps/sentence/32.wav")
        time.sleep(5)
        a = random.randint(1, 2)
        if a == 1:
          self.pattern41()
        else:
          self.pattern42()
    def pattern33(self):
        time.sleep(4)
        self.play("./apps/sentence/33.wav")
        self.pattern42()
    def pattern34(self):
        time.sleep(4)
        self.play("./apps/sentence/342.wav")
        a = random.randint(1, 2)
        if a == 1:
          self.pattern54()
        else:
          self.pattern43()
    def pattern41(self):
        time.sleep(2)
        self.play("./apps/sentence/41.wav")
        a = random.randint(1, 3)
        if a == 1:
          self.pattern51()
        elif a == 2:
          self.pattern52()
        elif a == 3:
          self.pattern53()
    def pattern42(self):
        self.play("./apps/sentence/421.wav")
        self.play("./apps/sentence/422.wav")
        self.pattern805()
    def pattern43(self):
        self.play("./apps/sentence/431.wav")
        time.sleep(6)
        self.play("./apps/sentence/432.wav")
        self.play("./apps/sentence/433.wav")
        a = random.randint(1, 2)
        if a == 1:
          self.pattern55()
        else:
          self.pattern56()
    def pattern51(self):
        time.sleep(2)
        self.play("./apps/sentence/511.wav")
        self.play("./apps/sentence/512.wav")
        a = random.randint(1, 2)
        if a == 1:
          self.pattern61()
        else:
          self.pattern621()
    def pattern52(self):
        time.sleep(2)
        self.play("./apps/sentence/52.wav")
        a = random.randint(1, 2)
        if a == 1:
          self.pattern622()
        elif a == 2:
          self.pattern63()
    def pattern53(self):
        time.sleep(2)
        self.play("./apps/sentence/53.wav")
        self.pattern804()
    def pattern54(self):
        time.sleep(1)
        self.play("./apps/sentence/54.wav")
        self.pattern806()
    def pattern55(self):
        time.sleep(1)
        time.sleep(1)
        self.play("./apps/sentence/55.wav")
        self.play("./apps/sentence/1001.wav")
        a = random.randint(1, 2)
        if a == 1:
          self.pattern64()
        elif a == 2:
          self.pattern65()
    def pattern56(self):
        time.sleep(1)
        time.sleep(1)
        self.play("./apps/sentence/56.wav")
        self.pattern65()
    def pattern57(self):
        self.play("./apps/sentence/432.wav")
        self.play("./apps/sentence/57.wav")
        self.play("./apps/sentence/1001.wav")
        time.sleep(5)
        a = random.randint(1, 2)
        if a == 1:
          self.play("./apps/sentence/341.wav")
          self.play("./apps/sentence/343.wav")
          self.pattern34()
        elif a == 2:
          self.pattern65()
    def pattern61(self):
        time.sleep(1)
        self.play("./apps/sentence/61.wav")
        self.pattern71()
    def pattern621(self):
        time.sleep(1)
        self.play("./apps/sentence/621.wav")
        self.pattern72()
    def pattern622(self):
        time.sleep(1)
        self.play("./apps/sentence/622.wav")
        self.pattern72()
    def pattern63(self):
        time.sleep(1)
        self.play("./apps/sentence/63.wav")
        self.pattern73()
    def pattern64(self):
        time.sleep(1)
        self.play("./apps/sentence/7.wav")
        self.play("./apps/sentence/342.wav")
        self.pattern807()
    def pattern65(self):
        time.sleep(1)
        self.play("./apps/sentence/651.wav")
        self.play("./apps/sentence/652.wav")
        self.pattern808()
    def pattern71(self):
        time.sleep(1)
        self.play("./apps/sentence/711.wav")
        self.play("./apps/sentence/712.wav")
        self.pattern801()
    def pattern72(self):
        time.sleep(3)
        a = random.randint(1, 2)
        if a == 1:
          self.play("./apps/sentence/721.wav")
          self.play("./apps/sentence/342.wav")
          self.pattern802()
        else:
          self.play("./apps/sentence/632.wav")
          self.pattern73()
    def pattern73(self):
        time.sleep(2)
        self.play("./apps/sentence/721.wav")
        self.play("./apps/sentence/73.wav")
        self.pattern803()
    def pattern801(self):
        time.sleep(1)
        self.play("./apps/sentence/73.wav")
        self.play("./apps/sentence/802.wav")
    def pattern802(self):
        time.sleep(1)
        self.play("./apps/sentence/803.wav")
        self.play("./apps/sentence/804.wav")
    def pattern803(self):
        time.sleep(1)
        self.play("./apps/sentence/802.wav")
    def pattern804(self):
        time.sleep(1)
        self.play("./apps/sentence/805.wav")
        self.play("./apps/sentence/806.wav")
    def pattern805(self):
        time.sleep(1)
        self.play("./apps/sentence/809.wav")
        self.play("./apps/sentence/806.wav")
    def pattern806(self):
        time.sleep(1)
        time.sleep(1)
        self.play("./apps/sentence/808.wav")
        self.play("./apps/sentence/802.wav")
    def pattern807(self):
        time.sleep(1)
        time.sleep(1)
        self.play("./apps/sentence/73.wav")
        self.play("./apps/sentence/802.wav")
    def pattern808(self):
        time.sleep(2)
        self.play("./apps/sentence/805.wav")
        self.play("./apps/sentence/806.wav")
    def pattern809(self):
        time.sleep(1)
        self.play("./apps/sentence/807.wav")
        self.play("./apps/sentence/805.wav")
        self.play("./apps/sentence/806.wav")
    
def main():
    d = play()
    d.play("./apps/sentence/1.wav")
    a = random.randint(1, 5)
    time.sleep(3)
    d.play("./apps/sentence/01.wav")
    d.play("./apps/sentence/901.wav")
    time.sleep(2)
    if a == 1:
      d.pattern21()
    elif a == 2:
      d.pattern22()
    elif a == 3:
      d.pattern23()
    elif a == 4:
      d.pattern24()
    else:
      d.pattern25()

if __name__ == '__main__':
    main()
