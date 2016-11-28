import subprocess
import time
import json
from camera import camera_thread
from camera import distant_thread
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

#proc_motor = subprocess.Popen(
#    ['./motor/motor'],
#    stdin = subprocess.PIPE,
#    stdout = subprocess.PIPE
#)

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
    thread = camera_thread.CameraThread(request, log, proc_app, proc_camera)
    thread.start()

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
    thread = distant_thread.DistantThread(request, log, proc_app, proc_sensor)
    thread.start()

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
    if request['module'] == 'camera':
        func_camera(request)
    elif request['module'] == 'voice':
        func_voice(request)
    elif request['module'] == 'motor':
        func_motor(request)
    elif request['module'] == 'sensor':
        func_sensor(request)
    elif request['module'] == 'speech':
        func_speech(request)
