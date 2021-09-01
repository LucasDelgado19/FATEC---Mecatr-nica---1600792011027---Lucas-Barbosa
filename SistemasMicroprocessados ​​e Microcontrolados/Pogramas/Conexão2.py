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

#Importa a biblioteca para fazer requisição
import urequests

dados = urequests.get("http://worldclockapi.com/api/json/utc/now")
data_hora = dados.json()["currentDateTime"]

print(data_hora)