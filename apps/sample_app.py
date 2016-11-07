from library import client
import time

while True:
    f = open('output', 'a')
    f.write(client.get_face_positions())
    f.close()
    time.sleep(2)

