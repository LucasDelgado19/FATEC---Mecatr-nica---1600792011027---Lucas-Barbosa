import esp32
import time
from machine import RTC

#Configurações globais
rtc = RTC()
rtc.datetime((2021, 8, 11, 2, 10, 25, 0, 0)) #set a specific date

#Converte de F para C
def converte_temperatura(tempf):
    return (tempf-32)*5/9

print('Monitoramente de Sensores:')

while True:
    #Ler sensores internos
    temperatura = esp32.raw_temperature()
    sensor_hall = esp32.raw_sensor()
    data_hora = rtc.datetime()

    #Exibir os valores dos sensores
    print('Temperatura:{} - {}'.format(onverte_temperatura(temperatura), data_hora))
    print('Hall:{} - {}'.format(sensor_hall, data_hora))
    time.sleep(2)