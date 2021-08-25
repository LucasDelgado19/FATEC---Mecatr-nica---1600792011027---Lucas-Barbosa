#Exemplo-INterrupcao
from machine import Pin, Timer
#Constante
LED_LIGADO = 0
LED_DESLIGADO = 1
BOTAO_ACIONADO = 0
BOTAO_DESACIONADO = 1

#Configurações
led1 = Pin(18, Pin.OUT, value=1)
led2 = Pin(19, Pin.OUT, value=1)
led3 = Pin(21, Pin.OUT, value=1)
bot1 = Pin(17, Pin.IN, Pin.PULL_UP)
bot2 = Pin(16, Pin.IN, Pin.PULL_UP)

#Variáveis globais
global tempo1
global tempo2
global tempo3
tempo1 = 0
tempo2 = 0
tempo3 = 0

#Funções que serão executadas quando o timer acontecer
def muda_tempos(t):
    global tempo1
    global tempo2
    global tempo3
    tempo1 += 1
    tempo2 += 1
    tempo3 += 1
    
def alterar_led_1():
    if led1.value() == LED_LIGADO:
        led1.value(LED_DESLIGADO)
    else:
        led1.value(LED_LIGADO)
        
def alterar_led_2():
    if led2.value() == LED_LIGADO:
        led2.value(LED_DESLIGADO)
    else:
        led2.value(LED_LIGADO)
        
def alterar_led_3():
    if led3.value() == LED_LIGADO:
        led3.value(LED_DESLIGADO)
    else:
        led3.value(LED_LIGADO) 
#Configura a interrupção
timer0 = Timer(0)
timer0.init(period=1000, mode=Timer.PERIODIC, callback=muda_tempos)
#Coloca um comportamento em caso de uma parada não esperada
try:
    while True:
        global tempo1
        global tempo2
        global tempo3
        if tempo1 == 1:
            tempo1 = 0
            alterar_led_1()
        if tempo2 == 2:
            tempo2 = 0
            alterar_led_2()
        if tempo3 == 10:
            tempo3 = 0
            alterar_led_3()
except Exception as e:
    print(str(e))
    timer0.deinit()
    led1.value(LED_DESLIGADO)
    led2.value(LED_DESLIGADO)
    led3.value(LED_DESLIGADO)