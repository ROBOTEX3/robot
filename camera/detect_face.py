import cv2
import json

capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while True:
    command = raw_input()
    if command == 'face_positions':
        _, img = capture.read()
        img = cv2.resize(img, (320, 240))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        response = {'faces': []}
        for (x, y, w, h) in faces:
            face = {
                'x': (x + (w / 2) - 160) / 320,
                'y': (y + (h / 2) - 120) / 120
            }
            response['faces'].append(face)
        print json.dumps(response)

