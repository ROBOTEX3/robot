import subprocess
import time
import json

proc_app = subprocess.Popen(
    ['python', '-u', './apps/sample_app.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)
proc_camera = subprocess.Popen(
    ['python', '-u', './camera/detect_face.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)
def func_camera(cmd):
    if cmd == 'face_positions':
        proc_camera.stdin.write(cmd + '\n')
        return proc_camera.stdout.readline()

while True:
    #get module and command from app
    # app_out, app_err = proc_app.communicate()
    request = json.loads(proc_app.stdout.readline())
    if request['module'] == 'camera':
        response = func_camera(request['command'])
    proc_app.stdin.write(response)
