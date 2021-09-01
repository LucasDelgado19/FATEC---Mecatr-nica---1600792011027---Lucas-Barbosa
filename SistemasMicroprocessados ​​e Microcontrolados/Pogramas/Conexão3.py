#Conecta em uma rede
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect ('BARBOSA/2G', '@ERBC#4590@')
        while not wlan.isconnected():
            pass
    print('Network config:', wlan.ifconfig())
    
do_connect()

def converterHora(horaStr):
    data,hora = horaStr.split('T')
    hora = hora[0:hora.find('Z')]
    ano,mes,dia = data.split('-')
    hora, minuto = hora.split(':')
    return {"ano": int(ano), "mes":int(mes), "dia":int(dia), "hora":int(hora), "minuto":int(minuto)}

#Importa a biblioteca para fazer requisição
import urequests

dados = urequests.get("http://worldclockapi.com/api/json/utc/now")
data_hora = dados.json()["currentDateTime"]

print(converterHora(data_hora))

