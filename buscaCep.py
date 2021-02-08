import requests
import re

""""""""
Essa API não aceita qualquer formato de CEP, então você tem que fazer regex no CEP e forçar o formato..
""""""""

cep = input("Digite o Cep: ")

def checar_cep(cep):
    pattern = r"^\d{5}-\d{3}$"
    return bool(re.findall(pattern, cep))

checar_cep(cep)
    
def buscar_naAPI():
    if checar_cep(cep):
        url = f'https://viacep.com.br/ws/{cep}/json/?callback=?'
        result = requests.get(url)
        result_dict = result.text
        print(result_dict)
    else:
        print("CEP inválido.")
    
buscar_naAPI()
