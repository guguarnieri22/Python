import requests

try:
    response = requests.get("https://sujeitoprogramador.com/r-api/?api=filmes", verify=False)
    if response.status_code == 200:
        filmes = response.json()
        for filme in filmes:
            print(f"{filme['id']} - {filme['titulo']}")

except requests.exceptions.RequestException as e:
    print("Erro ao obter a lista de filmes:", e)


filmes_em_cartaz = []


print("Lista dos Filmes em cartaz:\n")
for filme in filmes_em_cartaz:
    print(f"{filme['id']} - {filme['titulo']}")

while True:
    print("---MENU---\n 123 - Vingadores Ultimato\n 546 - Shazam!\n 125 - O Primeiro Homem\n 400 - Mission: Impossible – Fallout\n 554 - The Meg\n 987 - Venom\n 700 - Pacific Rim: A Revolta")
    print("1 - Ver detalhes do filme")
    print("2 - Fazer um comentário sobre o filme")
    print("3 - Excluir um comentário sobre o filme")
    print("0 - Sair")

    opcao = int(input())

    if opcao == 1:
        id_filme = int(input("\nDigite o id do filme: "))


        filme = next((f for f in filmes_em_cartaz if f["id"] == id_filme), None)

        if filme:
            print(f"\nSinopse do filme {filme['titulo']}:")
            print(filme["sinopse"])

            comentarios = filme.get("comentarios", [])
            if comentarios:
                print("\nComentários sobre o filme:\n")
                for comentario in comentarios:
                    print(f"{comentario['nome']}: {comentario['mensagem']}")
            else:
                print("\nAinda não há comentários sobre o filme.")
        else:
            print("\nFilme não encontrado.")

    elif opcao == 2:
        id_filme = int(input("\nDigite o id do filme: "))


        filme = next((f for f in filmes_em_cartaz if f["id"] == id_filme), None)

        if filme:
            nome = input("Digite o seu nome: ")
            mensagem = input("Digite o seu comentário: ")

            comentario = {"nome": nome, "mensagem": mensagem}

            comentarios = filme.get("comentarios", [])
            comentarios.append(comentario)

            filme["comentarios"] = comentarios

            print("\nComentário adicionado com sucesso.")
        else:
            print("\nFilme não encontrado.")

    elif opcao == 3:
        id_filme = int(input("\nDigite o id do filme: "))

        filme = next((f for f in filmes_em_cartaz if f["id"] == id_filme), None)

        if filme:
            comentarios = filme.get("comentarios", [])

            if comentarios:
                print("\nLista de comentários:\n")

                for i, comentario in enumerate(comentarios):
                    print(f"{i + 1} - {comentario['nome']}: {comentario['mensagem']}")

                id_comentario = int(input("Digite o número do comentário que deseja excluir: "))

                if id_comentario > 0 and id_comentario <= len(comentarios):
                    comentarios.pop(id_comentario - 1)
                    filme["comentarios"] = comentarios

                    print("\nComentário excluído com sucesso.")
                else:
                    print("\nNúmero de comentário inválido.")
            else:
                print("\nAinda não há comentários sobre o filme.")
        else:
            print("\nFilme não encontrado.")
