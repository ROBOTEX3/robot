#
# look this way (atti muite hoi)
#
# 2017/01/28 Saito Yuma
# 2017/01/31 finish game_start()

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
    time.sleep(4)
    client.speak('"If you failed three times, you lose."')
    time.sleep(4)
    client.speak('"OK?"')
    status['word'] = ''
    time.sleep(0.5)
    status['name'] = 'waiting-explain-response'
    while True:
        word = status['word']
        if word == 'yes':
            client.speak('"game start"')
            time.sleep(1)
            status['name'] = 'game-start'
            status['word'] = ''
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

def change_direction():
    """turn random."""
    status['ready'] = True
    word = status['word']
    if word == 'left':
        player['direction'] = 'left'
    elif word == 'right':
        player['direction'] = 'right'
    elif word == 'front':
        player['direction'] = 'front'
    #elif word == 'back':
    #    player['direction'] = 'back'
    else:
        status['ready'] = False

    if status['ready'] == False:
        client.speak('"Please say direction, Again"')
        time.sleep(3)
        status['name'] = 'game-start'
        status['word'] = ''
        game_start()
    else:
        status['ready'] = False
        i = random.randint(1, 3)
        if i == 1:
            maid['direction'] = 'left'
            maid['angle'] = -45
        elif i == 2:
            maid['direction'] = 'right'
            maid['angle'] = 45
        elif i == 3:
            maid['direction'] = 'front'
            maid['angle'] = 0
        #elif i == 4:
        #    maid['direction'] = 'back'
        #    maid['angle'] = 180
        client.left(maid['angle'])
        if maid['direction'] == 'front':
            time.sleep(1)
        else:
            time.sleep(3)
        client.right(maid['angle'])
        if maid['direction'] == 'front':
            time.sleep(1)
        else:
            time.sleep(3)
        # adjust_face_position()
        judge_game()
        
def judge_game():
    maid['count'] += 1
    if player['direction'] == maid['direction']:
        client.speak('"You Win"')
        time.sleep(3)
        status['name'] = 'game-end'
    elif maid['count'] >= 3:
        client.speak('"You lose"')
        time.sleep(3)
        status['name'] = 'game-end'
    else:
        client.speak('"Once more chance"')
        time.sleep(3)
        status['name'] = 'game-start'
        status['word'] = ''
        game_start()


def camera_listener(request):
    faces = request['faces']
    if status['name'] == 'getting-face':
        getting_face(faces)

def voice_listener(word):
    #elif status['name'] == 'get-direction':
    #    get_direction(word)

    # noise canceling
    if word in ('left', 'right', 'front', 'yes', 'no', 'exit'):
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




