import requests
import json


def pegar_estado():
    x = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
    dados = json.loads(x.content)
    return dados
