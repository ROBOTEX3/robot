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

proc_voice = subprocess.Popen(
    ['python', '-u', './voice/voice.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

proc_motor = subprocess.Popen(
    ['./motor/motor'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

proc_distant = subprocess.Popen(
    ['./sensor/distant'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
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
    log.communication('voice: send' + cmd)
    if cmd == 'recognize':
        proc_voice.stdin.write(cmd + '\n')
        response = proc_voice.stdout.readline()
    log.communication('voice: receive ' + response)
    return response

def func_motor(request):
    cmd = request['command']
    if cmd == 'stop':
        log.communication('motor: send' + cmd)
        proc_motor.stdin.write(cmd + '\n')
    elif cmd == 'move' or cmd == 'back':
        right_speed = request['right_speed']
        left_speed = request['left_speed']
        log.communication('motor: send' + cmd + ' ' + right_speed + ' ' + left_speed)
        proc_motor.stdin.write(cmd + ' ' + right_speed + ' ' + left_speed + '\n')
    elif cmd == 'right' or cmd == 'left':
        speed = request['speed']
        log.communication('motor: send' + cmd + ' ' + speed)
        proc_motor.stdin.write(cmd + ' ' + speed + '\n')

def func_sensor(request):
    cmd = request['command']
    log.communication('sensor: send' + cmd)
    if cmd == 'check':
        response = proc_sensor.stdin.write(cmd + '\n')
    log.communication('sensor: receive ' + response)
    return response

while True:
    #get module and command from app
    raw_request = proc_app.stdout.readline()
    log.communication('app: receive ' + raw_request)
    request = json.loads(raw_request)
    respnose = ''
    if request['module'] == 'camera':
        response = func_camera(request)
    elif request['module'] == 'voice':
        response = func_voice(request)
    elif request['module'] == 'motor':
        func_motor(request)
    elif request['module'] == 'sensor':
        response = func_sensor(request)
    log.communication('app: send ' + response)
    proc_app.stdin.write(response)
