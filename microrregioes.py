import requests

url = 'https://servicodados.ibge.gov.br/api/v1/localidades/microrregioes?view=nivelado'
headers = {'Accept': 'application/json'}
#auth = ('username', 'userpass')
print ('teste alteraçao do git')
response = requests.get(url, headers=headers)
print(response.content)
with open('Micro_regioes.json', 'wb') as outf:
    outf.write(response.content)