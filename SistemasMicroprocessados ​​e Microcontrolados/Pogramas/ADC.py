from machine import ADC, Pin, Timer
import machine
import time
import esp32

#Configuração inicial
adc = ADC(Pin(36))
#Ajusta o valor máximo de tensão para 3.6v
adc.atten(ADC.ATTN_11DB)


#Interrupção de tempo vinda do relógio RTC
#rtc = machine.RTC()
#rtc.datetime((2021, 9, 8, 10, 18, 0, 0, -3))
#rtc.alarm(RTC.ALARM0, time=2000, repeat=True)
#rtc.irq(RTC.ALARM0, handler=None, wake=machine.SLEEP)


#Coloca um comportamento em caso de uma parada não esperada
try:
    while True:
        valor_bits = adc.read()
        valor_volts = valor_bits*3.3/((2**12)-1)
        valor_hall = esp32.hall_sensor()     # read the internal hall sensor
        valor_temp_chip = (esp32.raw_temperature()-32)*5/9 # read the internal temperature of the MCU, in Fahrenheit
        saida = {'entrada_analogica_raw':valor_bits,
                 'entrada_analogica':valor_volts,
                 'sensor_hall':valor_hall,
                 'tempratura_chip':valor_temp_chip}
        print(saida)
        time.sleep(0.01)
        machine.lightsleep(10000)
except:
    print('Algo deu errado')
    #rtc.deinit()