import time
from library import client
import threading 
import wav_play.py
import pdb
import numpy as np
import scipy.io.wavfile as scw
import wave
import subprocess as subp
import pygame.mixer

#calc
def calc_match_bpm(data,bpm):
    N = len(data)
    f_bpm = bpm / 60
    f_frame = 44100 / 512
            
    phase_array = np.arange(N) * 2 * np.pi * f_bpm / f_frame
    sin_match = (1.0/N) * sum( data * np.sin(phase_array))
    cos_match = (1.0/N) * sum( data * np.cos(phase_array))

    return np.sqrt(sin_match ** 2 + cos_match ** 2)
                            
#return match level of sevelal bpm
def calc_all_match(data):
    match_list = []
    bpm_iter = range(60,300)
      
    #calc match level of sevelal bpm
    for bpm in bpm_iter:
        match = calc_match_bpm(data,bpm)
        match_list.append(match)
    return match_list

def return_beat():
    #load data
    src_name = "./app/sound/tempo_120.wav"
                            
    rate, dt = scw.read(src_name)
    dt = dt / (2 ** 15) #normalize
    sample_total = dt.size
    ts = 1.0 / rate  # sampling freakency
                                            
    # creat sound data about sevelal bpm
    # calc f_width square
    frame_size = 512
    sample_max = sample_total - (sample_total % frame_size) #cut rest
    frame_max = sample_max / frame_size
    frame_list = np.hsplit(dt[:sample_max],frame_max)
    amp_list = np.array([np.sqrt(sum(x ** 2)) for x in frame_list])
                               
    # get sound 
    amp_diff_list = amp_list[1:] - amp_list[:-1]
    amp_diff_list = np.vectorize(max)(amp_diff_list,0) #
    match_list = calc_all_match(amp_diff_list)      #
    most_match = match_list.index(max(match_list))  # 
    bpm = most_match+60                            # 
    return (bpm, src_name)


class MainThread(threading.Thread):
    def __init__(self):
          super(MainThread, self).__init__()
    def run(self):
        flg = True
        #sound = pygame.mixer.Sound("./sound/tempo_120.wav")    
        tempo = 120.0/60
    
        #wf = wave.open('./sound/tempo_120.wav')
        pygame.mixer.init()
        pygame.mixer.music.load("./apps/sound/tempo_120.wav")
        pygame.mixer.music.play(-1)
        time.sleep(2)
        #sound.play()
        for i in range(5):
            flg = not flg
            if flg:
                client.right(30)
            else:
                client.left(30)
            time.sleep(tempo)    

        pygame.mixer.music.stop()
        time.sleep(1)
        client.speak('"I am so tired"')


thread = MainThread()
client.startListener(thread)


    
