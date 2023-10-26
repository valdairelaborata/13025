import requests

# Fazer uma requisição GET a uma URL
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Verificar se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    data = response.json()  # Converter a resposta JSON para um dicionário
    print("Título:", data["title"])
    print("Corpo:", data["body"])
else:
    print("Erro na requisição:", response.status_code)
