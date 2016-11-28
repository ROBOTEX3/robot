from library import client
import time

while True:
    time.sleep(10)
    distant = client.get_distant(
        lambda request:
            if request['right'] < 40 or request['left'] < 40:
                client.speak("stopping")
    )
    faces = client.get_face_positions(
        lambda request:
            if len(faces['faces']) > 0:
                client.speak('found')
    )
