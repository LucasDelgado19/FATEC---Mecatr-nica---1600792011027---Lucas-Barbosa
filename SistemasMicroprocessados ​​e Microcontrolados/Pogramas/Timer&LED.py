#Interrupção
from machine import Pin
from time import sleep
import time

#Constante
LED_LIGADO = 0
LED_DESLIGADO = 1
BOTAO_ACIONADO = 0
BOTAO_DESACIONADO = 1

#configurações
led1 = Pin(18, Pin.OUT, value=1)
led2 = Pin(19, Pin.OUT, value=1)
led3 = Pin(21, Pin.OUT, value=1)
bot1 = Pin(17, Pin.IN, Pin.PULL_UP)
bot2 = Pin(16, Pin.IN, Pin.PULL_UP)

#Função que sera executada quando o timer acontecer
def alterar_led_1(t):
    if led1.value() == LED_LIGADO:
        led1.value(LED_DESLIGADO)
    else:
        led1.value(LED_LIGADO)
def alterar_led_2(t):
    if led2.value() == LED_LIGADO:
        led2.value(LED_DESLIGADO)
    else:
        led2.value(LED_LIGADO)
    
#Configurar a interrupção
Timer0 = Timer(0)
Timer1 = Timer(1)

timer0.init(period=1000, mode=Timer.ONE_SHOT, callback=alterar_led_1)
timer1.init(period=2000, mode=Timer.PERIODIC, callback=altera_led_2)


#Coloca um comportamento no caso de uma parada não esperada
try:
    while True:
        pass
except:
    timer0.deinit()
    timer1.deinit()
    led1.value(LED_DESLIGADO)
    led2.value(LED_DESLIGADO)