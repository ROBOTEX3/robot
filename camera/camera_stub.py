import json
import time
import requests

while True:
    command = raw_input()
    if command == 'face_positions':
        requests.post('http://localhost:3000/camera/face_detection')
    time.sleep(2)
    print json.dumps({'faces': []})
