from machine import Pin
from time import sleep

led1 = Pin(18, Pin.OUT, value=1)
led2 = Pin(19, Pin.OUT, value=1)
led3 = Pin(21, Pin.OUT, value=1)
bot1 = Pin(17, Pin.IN, Pin.PULL_UP)
bot2 = Pin(16. Pin.IN, Pin.PULL_UP)

try:
    carga_intervalo_led1 = 2
    carga_intervalo_led2 = 1
    intervalo_led1 = carga_intervalo_led1
    intervalo_led2 = carga_intervalo_led2
    while True:
        sleep(0.5)
        intervalo_led1 = intervalo_led1 - 1
        intervalo_led2 -= 1
        #Testa se já passou 1 segundo
        if intervalo_led1 == 0:
            intervalo_led1 = carga_intervalo_led1
            if led1.value() == 0:
                led1.value(1)
        else:
            led1.value(0)
        #Testa se já passou 0.5 segundo
        if intervalo_led2 == 0:
            intervalo_led2 = carga_intervalo_led2
            if led2.value() == 0:
                led2.value(1)
            else: led2.value(0)
except:
    led1.value(1)
    led2.value(1)