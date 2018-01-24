import platform
import json as j
from urllib import request as r

url = r.urlopen('http://ip-api.com/json').read()
jsn = j.loads(url.decode('UTF-8'))

print ('\n\nDados do Computador:\n')
print('Tipo de Sistema Operacional:  ' + platform.system())
print ('Tipo de Máquina:  ' + platform.machine())
print('Processador:  ' + platform.processor())
print('Nome da rede do computador:  ' + platform.node())
print('Nome do sistema operacional:  ' + platform.platform())


print('\nDados de Localização: \n')
print('Cidade:  ' + jsn['city'])
print('Estado:  ' + jsn['regionName'])
print('Sigla do estado:  ' + jsn['region'])
print('Tipo de fuso horário:  ' + jsn['timezone'])
print('País:  ' + jsn['country'])
print('Sigla do país:  ' + jsn['countryCode'])
print('Latitude:  ' + str(jsn['lat']))
print('longitude:  ' + str(jsn['lon']))


print('\nDados sobre a conexão:\n')
print('Provedor de internet:  ' + jsn['isp'])
print('Empresa prestadora do serviço:  ' + jsn['as'])
print('IP da máquina:  ' + jsn['query'])
