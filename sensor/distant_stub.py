import json
import time
import requests
import sys

argv = sys.argv

url = argv[1]

while True:
    input = raw_input()
    r = requests.post(url + '/sensor/distant')
    time.sleep(1)
    print r.text
