import subprocess
import time

proc = subprocess.Popen(
    ['python', '-u', 'detect_face.py'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)

while True:
    proc.stdin.write('check\n')
    print proc.stdout.readline()
    time.sleep(2)
