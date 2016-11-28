from library import client
import time

while True:
    time.sleep(1)
    distant = client.get_distant()
    faces = client.get_face_positions()
    if distant['right'] < 40 or distant['left'] < 40:
        client.speak("stopping")
        client.stop()
    else:
        client.move(300, 300)
    if len(faces['faces']) > 0:
        client.speak('"found you"')
