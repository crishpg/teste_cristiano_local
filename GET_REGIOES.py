import requests

url = 'https://servicodados.ibge.gov.br/api/v1/localidades/regioes?orderBy=nome'
headers = {'Accept': 'application/json'}
#auth = ('username', 'userpass')
response = requests.get(url, headers=headers)

with open('regioes.json', 'wb') as outf:
    outf.write(response.content)