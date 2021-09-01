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
#data e hora atual

dados = urequests.get("http://worldclockapi.com/api/json/utc/now")
data_hora = dados.json()["currentDateTime"]
data_hora = converterHora(data_hora)
#temperatura atual
dados = urequests.get("https://api.openweathermap.org/data/2.5/weather?q=São%20Paulo,BR-SP&appid=ff697221ef13be4781a23897b8d24513")
dados = dados.json()
temperatura = dados["main"]["temp"]-273.15

print("Data atual:", data_hora)
print("Temperatura atual:", temperatura)
