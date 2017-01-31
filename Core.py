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

proc = {}

proc['app'] = subprocess.Popen(
    ['python', '-u', './apps/app1.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

nullFile = open('/dev/null', 'w')

def changeApp(app):
    proc['app'] = subprocess.Popen(
        ['python', '-u', './apps/' + app],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE
    )
    for thread in threads.values():
        thread.changeApp(proc['app'])
    return proc['app']

def exitCore():
    app = proc.pop('app')
    for process in proc.values():
        process.terminate()
    app.terminate()
    sys.exit()

if not is_test:
    proc['julius'] = subprocess.Popen(
        ['../dvd/julius/julius-4.2.3/julius/julius', '-C', 'voice/rapiro.jconf', '-module'],
        stdout=nullFile
    )
time.sleep(3)

if is_test:
    camera_cmd = ['python', '-u', './camera/camera_stub.py', url]
else:
    camera_cmd = ['python', '-u', './camera/camera.py']
proc['camera'] = subprocess.Popen(
    camera_cmd,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

if is_test:
    voice_cmd = ['python', '-u', './voice/voice_stub.py', url]
else:
    voice_cmd = ['python', '-u', './voice/connection.py']
proc['voice'] = subprocess.Popen(
    voice_cmd,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

if is_test:
    motor_cmd = ['python', '-u', './motor/motor_stub.py', url]
else:
    motor_cmd = ['./motor/motor_v3']
proc['motor'] = subprocess.Popen(
    motor_cmd,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

if is_test:
    distant_cmd = ['python', '-u', './sensor/distant_stub.py', url]
else:
    distant_cmd = ['./sensor/distant']
proc['sensor'] = subprocess.Popen(
    distant_cmd,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

if is_test:
    speech_cmd = ['python', '-u', './simple_stub.py']
else:
    speech_cmd = ['python', '-u', './speech/speech.py']
proc['speech'] = subprocess.Popen(
    speech_cmd,
    stdin = subprocess.PIPE,
    stdout = nullFile,
    stderr = nullFile
)

if is_test:
    shoe_cmd = ['python', '-u', './simple_stub.py']
else:
    shoe_cmd = ['python', '-u', './shoe/shoe.py']
proc['shoe'] = subprocess.Popen(
    shoe_cmd,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

threads = {}

def func_camera(request):
    threads['camera'] = camera_thread.CameraThread(request, log, proc['app'], proc['camera'])
    threads['camera'].start()

def func_voice():
    thread = voice_thread.VoiceThread(
        log,
        proc['app'],
        proc['voice'],
        changeApp,
        exitCore
    )
    thread.start()

def func_shoe():
    threads['shoe'] = shoe_thread.ShoeThread(log, proc['app'], proc['shoe'])
    threads['shoe'].start()

def func_motor(request):
    cmd = request['command']
    if cmd == 'stop':
        log.communication('motor: send ' + cmd)
        proc['motor'].stdin.write(cmd + '\n')
    elif cmd == 'move' or cmd == 'back':
        right_speed = request['left_speed']
        left_speed = request['right_speed']
        right = str(right_speed)
        left = str(left_speed)
        log.communication('motor: send ' + cmd + ' ' + right + ' ' + left)
        proc['motor'].stdin.write('move_spd ' + right + ' ' + left + '\n')
    elif cmd == 'right' or cmd == 'left':
        angle = request['angle']
        log.communication('motor: send ' + cmd + ' ' + str(angle))
        proc['motor'].stdin.write(cmd + ' ' + str(angle) + '\n')
    elif cmd == 'move_acc':
        dst = request['dst']
        log.communication('motor: send ' + cmd + ' ' + str(dst))
        proc['motor'].stdin.write('move ' + str(dst) + ' ' + str(dst) + '\n')

def func_sensor(request):
    threads['sensor'] = distant_thread.DistantThread(request, log, proc['app'], proc['sensor'])
    threads['sensor'].start()

def func_speech(request):
    cmd = request['command']
    if cmd == 'speak':
        msg = request['message']
        log.communication('speech: send ' + msg)
        proc['speech'].stdin.write(msg + '\n')

# start voice thread
func_voice()
func_shoe()

while True:
    #get module and command from app
    raw_request = proc['app'].stdout.readline()
    try:
        request = json.loads(raw_request)
    except ValueError:
        continue
    log.communication('app: receive ' + raw_request)
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
