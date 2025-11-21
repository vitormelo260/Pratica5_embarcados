#!/home/sel/VitorJoao/bin/python3
#Indica que o interpretador Python 3 deve ser utilizado e o diretório em que ele está localizado.
import RPi.GPIO as GPIO #Importa a bibilioteca RPi.GPIO e a nomeia com GPIO.
from time import sleep #Importa a função sleep.

GPIO.setmode(GPIO.BCM) #Define o modo de numeração dos pinos de acordo com o BCM, independente da posição física na placa.
GPIO.setup(17,GPIO.OUT) #Configura o GPIO17 como output
GPIO.setup(18,GPIO.OUT) #Configura o GPIO18 como output

GPIO.output(17,True) #Atribui nível lógico alto ao GPIO17
GPIO.output(18,False) #Atribui nível lógico alto ao GPIO18
print("Led desligado") #Imprime a mensagem no terminal

