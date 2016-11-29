import json
import time
import requests

while True:
    input = raw_input()
    r = requests.post('http://localhost:3000/sensor/distant')
    time.sleep(1)
    print r.text
