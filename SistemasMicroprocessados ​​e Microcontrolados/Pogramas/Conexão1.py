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

dados = urequests.request("GET", "https://viacep.com.br/ws/03245000/json/")
# dados = urequests.get("site-URL")
print(dados.text)