import json
import time

while True:
    raw_input()
    time.sleep(1)
    print json.dumps({'right': 100, 'left': 100})
