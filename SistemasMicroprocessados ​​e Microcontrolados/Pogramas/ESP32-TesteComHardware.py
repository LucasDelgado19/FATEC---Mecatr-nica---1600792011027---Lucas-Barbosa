from machine import Pin
from time import sleep

led1 = Pin(18, Pin.OUT)
led2 = Pin(19, Pin.OUT)
led3 = Pin(21, Pin.OUT)
bot1 = Pin(17, Pin.IN, Pin.PULL_UP)
bot2 = Pin(16. Pin.IN, Pin.PULL_UP)

led1.value(0)
led2.value(0)
led3.value(0)

sleep(2)

led1.value(1)
led2.value(1)
led3.value(1)

print('Estado do Botão 1: {}'. format(bot1.value()))
print('Estado do Botão 2: {}'. format(bot2.value()))