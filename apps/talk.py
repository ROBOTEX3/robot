import wave
import time
import pyaudio
import random
import sample_chat_short
import sample_chat_long

def main():
     d = sample_chat_short.play()
     d.play("sentence/01.wav")
     a = random.randint(1, 3)
     if a == 1:
       sample_chat_long.main()
     elif a == 2:
       d.play("sentence/1100.wav")
       d.play("sentence/1101.wav")
       d.play("sentence/806.wav")
     else:
       sample_chat_short.main()

if __name__ == '__main__':
    main()
