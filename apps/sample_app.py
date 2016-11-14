from library import client
import time

while True:
    client.move(100, 100)
    distant = client.get_distant()
    if distant['right'] < 40 or distant['left'] < 40:
        client.stop()

