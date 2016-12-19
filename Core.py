import subprocess
import time
import json
import sys
from camera import camera_thread
from sensor import distant_thread
from voice import voice_thread
from shoe import shoe_thread
from library import log

argv = sys.argv
if len(argv) > 1:
    is_test = argv[1] == 'test'
else:
    is_test = False

url = 'http://localhost:3000'

proc_app = subprocess.Popen(
    ['python', '-u', './apps/sample_shoe.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)


if is_test:
    camera_cmd = ['python', '-u', './camera/camera_stub.py', url]
else:
    camera_cmd = ['python', '-u', './camera/camera.py']
proc_camera = subprocess.Popen(
    camera_cmd,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

if is_test:
    voice_cmd = ['python', '-u', './voice/voice_stub.py', url]
else:
    voice_cmd = ['python', '-u', './voice/connection.py']
proc_voice = subprocess.Popen(
    voice_cmd,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

if is_test:
    motor_cmd = ['python', '-u', './motor/motor_stub.py', url]
else:
    motor_cmd = ['./motor/motor']
proc_motor = subprocess.Popen(
    motor_cmd,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

if is_test:
    distant_cmd = ['python', '-u', './sensor/distant_stub.py', url]
else:
    distant_cmd = ['./sensor/distant']
proc_sensor = subprocess.Popen(
    distant_cmd,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

if is_test:
    speech_cmd = ['python', '-u', './simple_stub.py']
else:
    speech_cmd = ['python', '-u', './speech/speech.py']
proc_speech = subprocess.Popen(
    speech_cmd,
    stdin = subprocess.PIPE
)

proc_shoe = subprocess.Popen(
    ['python', '-u', './shoe/shoe.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

def func_camera(request):
    thread = camera_thread.CameraThread(request, log, proc_app, proc_camera)
    thread.start()

def func_voice():
    thread = voice_thread.VoiceThread(log, proc_app, proc_voice)
    thread.start()

def func_shoe():
    thread = shoe_thread.ShoeThread(log, proc_app, proc_shoe)
    thread.start()

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

# start voice thread
func_voice()
func_shoe()

while True:
    #get module and command from app
    raw_request = proc_app.stdout.readline()
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
