import RPi.GPIO as GPIO
from time import sleep
from library import client
import threading
 
def clean_listener(self):
	GPIO.setmode(GPIO.BOARD)
	 
	Motor1A = 16
	Motor1B = 18
	Motor1E = 22
	 
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)
	 
	print "Going forwards"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	 
	sleep(2)
	 
	print "Now stop"
	GPIO.output(Motor1E,GPIO.LOW)
	 
	GPIO.cleanup()
	
class MainThread(threading.Thread):
	def __init__(self):
		super(MainThread, self).__init__()
	def run(self):
		clean_listener(self)
thread = MainThread()
client.startListener(thread)