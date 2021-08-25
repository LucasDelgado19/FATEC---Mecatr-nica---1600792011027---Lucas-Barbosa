#Interrupção
from machine import Pin
from time import sleep
import time

#Constante
LED_LIGADO = 0
LED_DESLIGADO = 1
BOTAO_ACIONADO = 0
BOTAO_DESACIONADO = 1

#variavel global
contador = 0
tempo_bot1 = time.ticks_ms()

#função que vai ser executada durante a interrupção
def minha_funcao(fonte):
    global tempo_bot1
    if abs(time.ticks_diff(tempo_bot1, time.ticks_ms())) > 200:
        tempo_bot1 = time.ticks_ms()
        global contador
        contador +=1
        print(contador,'- Aconteceu dentro da função!!')

    
#configurações
led1 = Pin(18, Pin.OUT, value=1)
led2 = Pin(19, Pin.OUT, value=1)
led3 = Pin(21, Pin.OUT, value=1)
bot1 = Pin(17, Pin.IN, Pin.PULL_UP)
bot2 = Pin(16, Pin.IN, Pin.PULL_UP)

#Configurar a interrupção
bot1.irq(minha_funcao, trigger=Pin.IRQ_FALLING)

#Coloca um comportamento no caso de uma parada não esperada
try:
    while True:
        pass
except:
    pass