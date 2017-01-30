import json
import threading

listeners = {
    'camera': [],
    'sensor': [],
    'voice': [],
    'shoe': []
}

class CallbackThread(threading.Thread):
    def __init__(self, callback, response):
        super(CallbackThread, self).__init__()
        self.callback = callback
        self.response = response
    def run(self):
        self.callback(self.response)

def startListener(thread):
    thread.start()
    while True:
        data = json.loads(raw_input())
        request = data['request']
        response = data['response']
        module = request['module']
        if len(listeners[module]) > 0:
            thread = CallbackThread(listeners[module][0], response)
            thread.start()
            listeners[module].pop(0)

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

def right(angle):
    request = {
        'module': 'motor',
        'command': 'right',
        'angle': angle
    }
    print json.dumps(request)

def left(angle):
    request = {
        'module': 'motor',
        'command': 'left',
        'angle': angle
    }
    print json.dumps(request)

def move_acc(dst):
    request = {
        'module': 'motor',
        'command': 'move_acc',
        'dst': dst
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

def get_voice(callback):
    listeners['voice'].append(callback)

def get_shoe(callback):
    listeners['shoe'].append(callback)

def speak(msg):
    request = {
        'module': 'speech',
        'command': 'speak',
        'message': msg
    }
    print json.dumps(request)
