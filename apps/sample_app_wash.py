import RPi.GPIO as GPIO
from time import sleep
from library import client
import threading

def wash_listener(self):
	GPIO.setmode(GPIO.BOARD)
	 
	Motor2A = 23
	Motor2B = 21
	Motor2E = 19
	 
	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)
	GPIO.setup(Motor2E,GPIO.OUT)
	 
	print "Going forwards"

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
	 
	sleep(3)
	 
	print "Going backwards"

	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	 
	sleep(3)
	 
	print "Now stop"
	GPIO.output(Motor2E,GPIO.LOW)
	 
	GPIO.cleanup()

class MainThread(threading.Thread):
	def __init__(self):
		super(MainThread, self).__init__()
	def run(self):
		wash_listener(self)
thread = MainThread()
client.startListener(thread)