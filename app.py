import requests


response = requests.get("https://viacep.com.br/ws/81710230/json/")

if response.status_code == 200:
    data = response.json()
    print(f'Olá eu moro na rua {data["logradouro"]}, no bairro {data["bairro"]}')
   

else:
    print("Erro ao tentar fazer o get")

    

