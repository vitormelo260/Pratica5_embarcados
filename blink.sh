#!/bin/bash
#Indica ao sistema operacional que deve-se utilizizar o interpretador Bash sheel.
echo 18 > /sys/class/gpio/export #Torna o GPIO18 acessível no espaço de usuário (exporta o pino GPIO18 e cria o diretório /sys/class/gpio/export)
echo out > /sys/class/gpio/gpio18/direction #Define o GPIO18 como output.

while [ 1 ] #loop infinito
	do 
		echo 1 > /sys/class/gpio/gpio18/value #Atribui 1 ("high") ao pino GPIO18.
		sleep 0.2s #Espera por 0.2 segundos com o valor anterior.
		echo 0 > /sys/class/gpio/gpio18/value #Define 0 como valor do GPIO18.
		sleep 0.2s #Espera por 0.2 segundos com o valor anterior.
	done
