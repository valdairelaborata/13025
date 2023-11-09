import requests


response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    data = response.json()

    print(data["title"])
    print(data["body"])
   

else:
    print("Erro ao tentar fazer o get")

