import requests

# Fazer uma requisição GET a uma URL
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    data = response.json()
    print(data)

else:     
    print("Erro na requisição:", response.status_code)    

