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

#proc_voice = subprocess.Popen(
#    ['python', '-u', './voice/voice.py'],
#    stdin = subprocess.PIPE,
#    stdout = subprocess.PIPE
#)

proc_motor = subprocess.Popen(
    ['./motor/motor'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

proc_sensor = subprocess.Popen(
    ['./sensor/distant'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

proc_speech = subprocess.Popen(
    ['python', '-u', './speech/speech.py'],
    stdin = subprocess.PIPE
)

def func_camera(request):
    cmd = request['command']
    log.communication('camera: send ' + cmd)
    if cmd == 'face_positions':
        proc_camera.stdin.write(cmd + '\n')
        response = proc_camera.stdout.readline()
    log.communication('camera: receive ' + response)
    return response

def func_voice(request):
    cmd = request['cmd']
    log.communication('voice: send ' + cmd)
    if cmd == 'recognize':
        proc_voice.stdin.write(cmd + '\n')
        response = proc_voice.stdout.readline()
    log.communication('voice: receive ' + response)
    return response

def func_motor(request):
    cmd = request['command']
    if cmd == 'stop':
        log.communication('motor: send ' + cmd)
        proc_motor.stdin.write(cmd + '\n')
    elif cmd == 'move' or cmd == 'back':
        right_speed = request['right_speed']
        left_speed = request['left_speed']
        right = str(right_speed)
        left = str(left_speed)
        log.communication('motor: send ' + cmd + ' ' + right + ' ' + left)
        proc_motor.stdin.write(cmd + ' ' + right + ' ' + left + '\n')
    elif cmd == 'right' or cmd == 'left':
        speed = request['speed']
        log.communication('motor: send ' + cmd + ' ' + str(speed))
        proc_motor.stdin.write(cmd + ' ' + str(speed) + '\n')

def func_sensor(request):
    cmd = request['command']
    log.communication('sensor: send ' + cmd)
    if cmd == 'check':
        proc_sensor.stdin.write(cmd + '\n')
        response = proc_sensor.stdout.readline()
    log.communication('sensor: receive ' + response)
    return response

def func_speech(request):
    cmd = request['command']
    if cmd == 'speak':
        msg = request['message']
        log.communication('speech: send ' + msg)
        proc_speech.stdin.write(msg + '\n')

while True:
    #get module and command from app
    raw_request = proc_app.stdout.readline()
    print raw_request
    log.communication('app: receive ' + raw_request)
    request = json.loads(raw_request)
    response = ''
    if request['module'] == 'camera':
        response = func_camera(request)
    elif request['module'] == 'voice':
        response = func_voice(request)
    elif request['module'] == 'motor':
        func_motor(request)
    elif request['module'] == 'sensor':
        response = func_sensor(request)
    elif request['module'] == 'speech':
        func_speech(request)
    print response
    log.communication('app: send ' + response)
    if response != '':
        proc_app.stdin.write(response)
