import requests
import json
import sys
import time

argv = sys.argv

url = argv[1]

while True:
    input = raw_input()
    request = input.split(' ')
    cmd = request[0]
    if cmd == 'move':
        right = request[1]
        left = request[2]
        requests.post(url + '/motor/move', params={
            'right': int(right), 'left': int(left)
        })
    elif cmd == 'stop':
        requests.post(url + '/motor/stop')
    elif cmd == 'left':
        angle = request[1]
        requests.post(url + '/motor/move', params={
            'right': int(angle) * -4, 'left': int(angle) * 4 
        })
        time.sleep(1)
        requests.post(url + '/motor/stop')
    elif cmd == 'right':
        angle = request[1]
        requests.post(url + '/motor/move', params={
            'right': int(angle) * 4, 'left': int(angle) * -4
        })
        time.sleep(1)
        requests.post(url + '/motor/stop')
