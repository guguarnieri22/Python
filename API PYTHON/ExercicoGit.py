import requests


cep = input("Digite o DEV desejado: ")
url = f"https://api.github.com/users/{login}"


response = requests.get(url)


if response.status_code == 200:
    dados = response.json()
    print(f"Name: {dados['name']}")
    print(f"public_repos: {dados['public_repos']}")
    print(f"followers: {dados['followers']}")

else:
    print("Dev não encontrado.")