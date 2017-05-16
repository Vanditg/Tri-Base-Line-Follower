import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

GPIO.output(36,0)
GPIO.output(40,0)
P=GPIO.PWM(38,100)

while 1:
	P.start(50)
	time.sleep(50)
