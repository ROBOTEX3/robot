import wave
import time
import pyaudio
import random
import sample_chat_short
import sample_chat_long

def main():
     a = random.randint(1, 2)
     if a == 1:
       sample_chat_long.main()
     else:
       sample_chat_short.main()

if __name__ == '__main__':
    main()
