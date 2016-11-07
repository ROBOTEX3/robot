import json

def get_face_positions():
    request = {
        'module': 'camera',
        'command': 'face_positions'
    }
    print json.dumps(request)
