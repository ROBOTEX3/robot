import subprocess
import time
import json
from library import log

proc_app = subprocess.Popen(
    ['python', '-u', './apps/sample_app.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

proc_camera = subprocess.Popen(
    ['python', '-u', './camera/camera.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

proc_void = subprocess.Popen(
    ['python', '-u', './voice/voice.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

def func_camera(cmd):
    log.communication('camera: send ' + cmd)
    if cmd == 'face_positions':
        proc_camera.stdin.write(cmd + '\n')
        response = proc_camera.stdout.readline()
    log.communication('camera: receive ' + response)
    return response

def func_voice(cmd):
    log.communication('voice: send' + cmd)
    if cmd == 'recognize':
        proc_voice.stdin.write(cmd + '\n')
        response = proc_voice.stdout.readline()
    log.communication('voice: receive ' + response)
    return response

while True:
    #get module and command from app
    raw_request = proc_app.stdout.readline()
    log.communication('app: receive ' + raw_request)
    request = json.loads(raw_request)
    if request['module'] == 'camera':
        response = func_camera(request['command'])
    elif request['module'] == 'voice':
        response = func_voice(request['command'])
    log.communication('app: send ' + response)
    proc_app.stdin.write(response)
