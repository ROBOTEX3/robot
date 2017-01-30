from library import client
import time
import threading
import math

status = {
    'name': 'searching-masaki'
}

def face_direction(face):
    x = face['x']
    if x > 0:
        client.right(int(30 * x))
    else:
        client.left(int(-30 * x))

def searching_masaki(faces):
    keys = faces.keys()
    keys = filter(lambda k: faces[k]['name'] == '', keys)
    if len(keys) == 0:
        client.right(30)
    else:
        status['name'] = 'facing-masaki'
    client.get_face_positions(camera_listener)

def facing_masaki(faces):
    keys = faces.keys()
    if len(keys) == 0:
        client.get_face_positions(camera_listener)
        return
    keys = filter(lambda k: faces[k]['name'] == '', keys)
    if len(keys) == 0:
        client.get_face_positions(camera_listener)
        return
    masakiFace = faces[keys[0]]
    if math.fabs(masakiFace['x']) < 0.1:
        client.move_acc(int(masakiFace['distance']))
        time.sleep(2)
        client.speak('"Hi, masaki."')
        time.sleep(1)
        client.speak('"give me coke"')
        status['name'] = 'waiting'
    else:
        face_direction(masakiFace)
        client.get_face_positions(camera_listener)

def searching_haruki(faces):
    keys = faces.keys()
    keys = filter(lambda k: faces[k]['name'] == 'haruki', keys)
    if len(keys) == 0:
        client.right(30)
    else:
        status['name'] = 'facing-haruki'
    client.get_face_positions(camera_listener)

def facing_haruki(faces):
    keys = faces.keys()
    if len(keys) == 0:
        client.get_face_positions(camera_listener)
        return
    keys = filter(lambda k: faces[k]['name'] == 'haruki', keys)
    if len(keys) == 0:
        client.get_face_positions(camera_listener)
        return
    masakiFace = faces[keys[0]]
    if math.fabs(masakiFace['x']) < 0.1:
        client.move_acc(int(masakiFace['distance']))
        time.sleep(2)
        client.speak('"Hi, haruki."')
        time.sleep(1)
        client.speak('"I have coke for you"')
        status['name'] = 'finished'
    else:
        face_direction(masakiFace)
        client.get_face_positions(camera_listener)

def waiting(word):
    if word == 'put':
        status['name'] = 'searching-haruki'
        client.get_face_positions(camera_listener)

def camera_listener(request):
    faces = request['faces']
    if status['name'] == 'searching-masaki':
        searching_masaki(faces)
    elif status['name'] == 'facing-masaki':
        facing_masaki(faces)
    elif status['name'] == 'facing-haruki':
        facing_haruki(faces)
    elif status['name'] == 'searching-haruki':
        searching_haruki(faces)

def voice_listener(word):
    if status['name'] == 'waiting':
        waiting(word)
    client.get_voice(voice_listener)

class MainThread(threading.Thread):
    def __init__(self):
       super(MainThread, self).__init__()
    def run(self):
        client.get_face_positions(camera_listener)
        client.get_voice(voice_listener)

thread = MainThread()
client.startListener(thread)
