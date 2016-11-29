import json
import time
import requests
import sys

argv = sys.argv

url = argv[1]

while True:
    command = raw_input()
    if command == 'face_positions':
        requests.post(url + '/camera/face_detection')
    time.sleep(2)
    print json.dumps({'faces': []})
