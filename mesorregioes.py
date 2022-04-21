import requests

url = 'https://servicodados.ibge.gov.br/api/v1/localidades/mesorregioes?orderBy=nome'
headers = {'Accept': 'application/json'}
#auth = ('username', 'userpass')
response = requests.get(url, headers=headers)
print(response.content)
with open('Mesoregioes.json', 'wb') as outf:
    outf.write(response.content)