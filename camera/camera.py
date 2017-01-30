import cv2
import cv2.cv as cv
import json
import os
import requests


personIds = {
    'a27c354a-2c0e-4b38-be6c-b64a2daf6b9e': 'haruki',
    '57888a6e-06fa-4fa8-b91e-9ebfb4102677': 'masaki',
    '4796cabc-dcba-4c88-b2c7-5db21a288175': 'yasutaka',
    '269a1a64-8686-4269-a582-60f2bd664b6b': 'yuma'
}

detect_headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '7f898d38a01240078533a69dd4e98d45'
}
identify_headers = {
    'Ocp-Apim-Subscription-Key': '7f898d38a01240078533a69dd4e98d45'
}
detect_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'
identify_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/identify'

while True:
    command = raw_input()
    if command == 'face_positions':
        capture = cv2.VideoCapture(0)
        _, img = capture.read()
        capture.release()
        img = cv2.resize(img, (320, 240))
        cv2.imwrite('tmp.jpg', img)
        f = open('tmp.jpg', 'rb')
        binary = f.read()
        f.close()
        res = requests.post(detect_url,
            headers = detect_headers,
            data = binary
        )
        faces = json.loads(res.text)
        faceIds = []
        response = {'faces': {}}
        for face in faces:
            faceIds.append(face['faceId'])
            pos = face['faceRectangle']
            data = {
                'x': (pos['left'] + (pos['width'] / 2) - 160) / 160.0,
                'y': (pos['top'] + (pos['height'] / 2) - 120) / 120.0,
                'name': ''
            }
            response['faces'][face['faceId']] = data
        if len(faces) > 0:
            res = requests.post(identify_url,
                headers = identify_headers,
                data = json.dumps({
                    'faceIds': faceIds,
                    'personGroupId': 'members'
                })
            )
            data = json.loads(res.text)
            for result in data:
                if len(result['candidates']) > 0:
                    personId = result['candidates'][0]['personId']
                    if personId in personIds:
                        response['faces'][result['faceId']]['name'] = personIds[personId]
        print json.dumps(response)

