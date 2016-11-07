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
		proc_camera.stdin.write(cmd)

while True:
	#get module and command from app
	time.sleep(1)
	app_out, app_err = proc_app.communicate()
	request = json.loads(app_out)
	if request['module'] == 'camera':
		func_camera(request['command'])
