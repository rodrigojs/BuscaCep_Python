import requests

def buscar():
    cep = input("Digite o Cep\n")
    url = f'https://viacep.com.br/ws/{cep}/json/?callback=?'
    result = requests.get(url)
    result_dict = result.text
    print(result_dict)


buscar()