#
# look this way (atti muite hoi)
#
# 2017/01/28 Saito Yuma
#

from library import client
import time
import threading
import random

status = {
    'name': 'getting-face',
    'ready': False,
    'word': ''
}
player = {
    'name': ' ',
    'direction': ' '
}
maid = {
    'direction': ' ',
    'angle': 0,
    'count': 0
}

def getting_face(faces):
    """start app and recognize player."""
    keys = faces.keys()
    if len(keys) != 0:
        player['name'] = faces[keys[0]]['name']
        client.speak('"Hi"')
        time.sleep(0.5)
        client.speak(player['name'])
        time.sleep(1)
        status['name'] = 'explain'
        explain()
    else:
        client.get_face_positions(camera_listener)

def explain():
    """explain rules of the game."""
    client.speak('"Lets play Look This Way!"')
    time.sleep(3)
    client.speak('"If I turn the direction you said, you win."')
    time.sleep(5)
    client.speak('"If you failed three times, you lose."')
    time.sleep(5)
    client.speak('"OK?"')
    time.sleep(0.5)
    status['name'] = 'waiting-explain-response'
    while True:
        if status['word'] == 'yes':
            client.speak('"game start"')
            time.sleep(1)
            status['name'] = 'get-direction'
            game_start()
        elif word == 'no':
            status['name'] = 'explain'
            explain()
        status['word'] = ''

def game_start():
    client.speak('"Look"')
    time.sleep(1)
    client.speak('"This"')
    time.sleep(1)
    client.speak('"Way!"')
    time.sleep(0.2)
    status['name'] = 'change-direction'
    change_direction()

def get_direction(word):
    """get direction from player."""
    if word == 'left':
        player['direction'] = 'left'
        status['ready'] = True
    elif word == 'right':
        player['direction'] = 'right'
        status['ready'] = True
    elif word == 'front':
        player['direction'] = 'front'
        status['ready'] = True
    elif word == 'back':
        player['direction'] = 'back'
        status['ready'] = True

def change_direction():
    """turn random."""
    if status['ready'] == False:
        client.speak('"Please say direction, Again"')
        time.sleep(3)
        status['name'] = 'get-direction'
        game_start()
    else:
        status['ready'] = False
        i = random.randint(1, 4)
        if i == 1:
            maid['direction'] = 'left'
            maid['angle'] = -90
        elif i == 2:
            maid['direction'] = 'right'
            maid['angle'] = 90
        elif i == 3:
            maid['direction'] = 'front'
            maid['angle'] = 0
        elif i == 4:
            maid['direction'] = 'back'
            maid['angle'] = 180
        client.left(maid['angle'])
        time.sleep(3)
        client.right(maid['angle'])
        judge-game()
        
def judge_game():
    maid['count'] += 1
    if player['direction'] == maid['direction']:
        client.speak('"You Win"')
        time.sleep(2)
        status['name'] = 'game-end'
    elif maid['count'] >= 3:
        client.speak('"You lose"')
        time.sleep(2)
        status['name'] = 'game-end'
    else:
        client.speak('"Once more chance"')
        time.sleep(2)
        status['name'] = 'get-direction'
        game_start()

def camera_listener(request):
    faces = request['faces']
    if status['name'] == 'getting-face':
        getting_face(faces)

def voice_listener(word):
    status['word'] = word
    client.get_voice(voice_listener)


class MainThread(threading.Thread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        client.get_face_positions(camera_listener)
        client.get_voice(voice_listener)

random.seed()
thread = MainThread()
client.startListener(thread)



 
