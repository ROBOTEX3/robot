import json
import time
import requests
import sys

argv = sys.argv

url = argv[1]

while True:
    time.sleep(1)
    r = requests.post(url + '/voice')
    print r.text
