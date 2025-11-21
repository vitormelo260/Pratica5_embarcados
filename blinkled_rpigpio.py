#!/home/sel/VitorJoao/bin/python3
#Indica o interpretador que deve ser utilizado (Python 3) e seu diretório. 
import RPi.GPIO as GPIO #Importa a biblioteca RPi.GPIO como GPIO 
from time import sleep #Importa a função sleep da biblioteca time

GPIO.setmode(GPIO.BCM) #Define os pinos da placa de acordo com o BCM e não com a numeração física.
GPIO.setup(18,GPIO.OUT) #Define o GPIO18 como output
GPIO.setup(17,GPIO.OUT) #Define o GPIO17 como output
while True:
	GPIO.output(17,False) #Atribui nivel lógico baixo para o GPIO17
	GPIO.output(18,True) #Atribui nivel lógico alto para o GPIO18
	sleep(1) #Pausa por 1 segundo
	print("Ligado") #Printa ligado no terminal
	GPIO.output(18,False) #Atribui nivel lógico baixo para o GPIO18
	sleep(1) #Pausa por 1 segundo
	print("Desligado") #Printa desligado no terminal
