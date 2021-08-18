from machine import Pin
from time import sleep

#Constantes
LED_LIGADO = 0
LED_DESLIGADO = 1
BOTAO_ACIONADO = 0
BOTAO_DESACIONADO = 1

led1 = Pin(18, Pin.OUT, value=1)
led2 = Pin(19, Pin.OUT, value=1)
led3 = Pin(21, Pin.OUT, value=1)
bot1 = Pin(17, Pin.IN, Pin.PULL_UP)
bot2 = Pin(16. Pin.IN, Pin.PULL_UP)

try:
    while True:
        #Lógica botão 1
        if bot1.value() == BOTAO_ACIONADO:
            led1.value(LED_LIGADO)
        else:
            led1.value(LED_DESLIGADO)
        #Lógica botão 2
        if bot2.value() == BOTAO_ACIONADO:
            led2.value(LED_LIGADO)
        else:
            led2.value(LED_DESLIGADO)
except:
    led1.value(LED_DESLIGADO)
    LED2.VALUE(LED_DESLIGADO)
    
#Outra maneira
try:
    while True:
        #Lógica botão 1
        led1.value(bot1.value())
        #Lógica botão 2
        led2.value(LED_LIGADO if bot2.value() == BOTAO_ACIONADO else LED_DESLIGADO)
except:
    led1.value(LED_DESLIGADO)
    led2.value(LED_DESLIGADO)
    
#Outra maneira (CÓDIGO COM PROBLEMA)
try:
    while True:
        #Lógica botão 1
        if bot1.value() == BOTAO_ACIONADO:
            if led1.value() == LED_LIGADO:
                led1.value(LED_DESLIGADO)
            else:
                led1.value(LED_LIGADO)
except:
    led1.value(LED_DESLIGADO)
#CÓDIGO SEM PROBLEMA
try:
    botao_ja_foi_acionado = False
    while True:
        #Lógica botão 1
        if bot1.value() == BOTAO_ACIONADO and not botao_ja_foi_acionado:
            sleep(0.25)
            botao_ja_foi_acionado = True
            if led1.value() == LED_LIGADO:
                led1.value(LED_DESLIGADO)
            else:
                led1.value(LED_LIGADO)
        elif bot1.value() == BOTAO_ACIONADO and botao_ja_foi_acionado:
            botao_ja_foi_acionado = False
except:
    led1.value(LED_DESLIGADO)