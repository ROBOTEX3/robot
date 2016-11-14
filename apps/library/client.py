import json

def get_face_positions():
    request = {
        'module': 'camera',
        'command': 'face_positions'
    }
    print json.dumps(request)
    return raw_input()

def move():
    request = {
        'module': 'motor',
        'command': 'move'
    }
    print json.dumps(request)

def stop():
    request = {
        'module': 'motor',
        'command': 'stop'
    }
    print json.dumps(request)

def back():
    request = {
        'module': 'motor',
        'command': 'stop'
    }
    print json.dumps(request)

def recongize_voice():
    request = {
        'module': 'voice',
        'command': 'recognize'
    }

