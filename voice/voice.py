import socket, re
import pygame.mixer

def catchSent(clientsock):
    flag=False
    answer=[]
    while True:
        recv_data = clientsock.recv(512)
    if re.search('<RECOGOUT>',recv_data):
        flag=True
    elif (flag==True):
        tmp = re.findall('<WHYPO WORD="[^"]+"',recv_data)
        for one in tmp:
            answer.append(one.split('"')[1])
        if re.search('</RECOGOUT>',recv_data):
            return(answer)

def analyze(sent):
    move = "S"
    if "左" in sent:
        move = "left"
    elif "右" in sent:
        move = "right"
    elif ("後ろ" in sent) or ("さがれ" in sent):
        move = "back"
    elif ("止まれ" in sent) or ("STOP" in sent) or ("とまれ" in sent):
        move = "stop"
    elif ("行け" in sent) or ("進め" in sent) or ("前" in sent):
        move = "go"
    elif ("balse" in sent):
        move = "quit"
    elif ("こんにちは"):
        move = "greeting"
        hoge = pygame.mixer.Sound("こんにちは.WAV")
        hoge.play()
    elif ("こんばんは"):
        move = "greeting"
        hoge = pygame.mixer.Sound("こんばんは.WAV")
        hoge.play()
    elif ("おやすみ"):
        move = "greeting"
        hoge = pygame.mixer.Sound("おやすみ.WAV")
        hoge.play()
    elif ("はじめまして"):
        move = "greeting"
        hoge = pygame.mixer.Sound("はじめまして.WAV")
        hoge.play()
    elif ("久しぶり"):
        move = "greeting"
        hoge = pygame.mixer.Sound("ひさしぶり.WAV")
        hoge.play()
    else:
        move = "other"
        hoge = pygame.mixer.Sound("もう一回.WAV")
        hoge.play()
    return(move)

Host = 'localhost'
Port = 10500 # Julius のポート番号
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((Host, Port)) 

while True:
    command = raw_input()
    if command == 'recognize':
        sent = catchSent(clientsock)
        show(sent)
        print analyze(sent)
