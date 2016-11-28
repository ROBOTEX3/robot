import json
import threading

listeners = {'camera': [], 'sensor': []}

class ListenerThread(threading.Thread):
    def __init__(self):
        super(ListenerThread, self).__init__()
    def run(self):
        while True:
            data = json.loads(raw_input())
            request = data['request']
            response = data['response']
            module = request['module']
            listeners[module][0](response)
            listeners[module].pop(0)

thread = ListenerThread()
thread.start()

def get_face_positions(callback):
    request = {
        'module': 'camera',
        'command': 'face_positions'
    }
    print json.dumps(request)
    listeners['camera'].append(callback)

def move(right_speed, left_speed):
    request = {
        'module': 'motor',
        'command': 'move',
        'right_speed': right_speed,
        'left_speed': left_speed
    }
    print json.dumps(request)

def stop():
    request = {
        'module': 'motor',
        'command': 'stop'
    }
    print json.dumps(request)

def back(right_speed, left_speed):
    request = {
        'module': 'motor',
        'command': 'stop',
        'right_speed': right_speed,
        'left_speed': left_speed
    }
    print json.dumps(request)

def right(speed):
    request = {
        'module': 'motor',
        'command': 'right',
        'speed': speed
    }
    print json.dumps(request)

def left(speed):
    request = {
        'module': 'motor',
        'command': 'left',
        'speed': speed
    }
    print json.dumps(request)

def recongize_voice():
    request = {
        'module': 'voice',
        'command': 'recognize'
    }
    print json.dumps(request)
    return json.loads(raw_input())

def get_distant(callback):
    request = {
        'module': 'sensor',
        'command': 'check'
    }
    print json.dumps(request)
    listeners['sensor'].append(callback)

def speak(msg):
    request = {
        'module': 'speech',
        'command': 'speak',
        'message': msg
    }
    print json.dumps(request)
