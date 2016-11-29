import requests
import json

while True:
    input = raw_input()
    request = input.split(' ')
    cmd = request[0]
    if cmd == 'move':
        right = request[1]
        left = request[2]
        requests.post('http://localhost:3000/motor/move', params={
            'right': right, 'left': left
        })
    elif cmd == 'stop':
        requests.post('http://localhost:3000/motor/stop')
