#!/home/sel/VitorJoao/bin/python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
while True:
	GPIO.output(17,False)
	GPIO.output(18,True)
	sleep(1)
	print("Ligado")
	GPIO.output(18,False)
	sleep(1)
	print("Desligado")
