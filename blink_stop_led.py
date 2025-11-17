#!/home/sel/VitorJoao/bin/python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.output(17,True)
GPIO.output(18,False)
print("Led desligado")

