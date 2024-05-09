import json
import urllib.request
cep=input('Digite o CEP: ')
url= f"https://viacep.com.br/ws/{cep}/json/"
try:
    response=urllib.request.urlopen(url)
    data=response.read().decode('utf-8')
    print(data)
except Exception as e:
    print(f'Erro: {e}')     