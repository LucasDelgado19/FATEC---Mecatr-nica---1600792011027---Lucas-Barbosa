from machine import Pin
import time

#Configura o LED Build in como saída
p2 = Pin(2,Pin.OUT)

#Roda um comportamento varias vezes
while True:
    #Coloca o pino em nivel alto
    p2.on()
    #Parar o microcontrolador por 1 segundo
    time.sleep(1)
    #Pedir para o microcontrolador desligar a saida
    p2.off()
    time.sleep(1)
