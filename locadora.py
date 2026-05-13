filmes = {}

def creat_filme():
    titulo = input("Digite o título do filme: ")
    filmes[titulo] = True
    diretor = input("Digite o nome do diretor: ")
    filmes[titulo] = diretor
    ano = input("Digite o ano de lançamento: ")
    filmes[titulo] = ano
    print("Filme cadastrado com sucesso!")

def delete_filme():
    titulo = input("Digite o título do filme a ser excluído: ")

    if titulo in filmes:
        del filmes[titulo]
        print("Filme removido com sucesso!")
    else:
        print("Filme não encontrado.")

def update_filme():
    titulo = input("Digite o título do filme a ser atualizado: ")

    if titulo in filmes:
        novo_titulo = input("Digite o novo título do filme: ")
        diretor = input("Digite o nome do novo diretor: ")
        ano = input("Digite o novo ano de lançamento: ")
        del filmes[titulo]
        filmes[novo_titulo] = (diretor, ano)
        print("Filme atualizado com sucesso!")
    else:
        print("Filme não encontrado.")

def list_filmes():
    print("\nFilmes cadastrados:")

    if len(filmes) == 0:
        print("Nenhum filme cadastrado.")
    else:
        for titulo in filmes:
            print(f"Título: {titulo}, Diretor: {filmes[titulo][0]}, Ano: {filmes[titulo][1]}")

# Menu principal
while True:
    print("\nBem-vindo ao sistema de gerenciamento de filmes!")
    print("Selecione uma opção:")
    print("1 - Cadastrar filmes")
    print("2 - Excluir filme")
    print("3 - Atualizar filme")
    print("4 - Listar filmes")
    print("5 - Sair")

    switch = input("Digite o número da opção desejada: ")

    if switch == "1":
        creat_filme()

    elif switch == "2":
        delete_filme()

    elif switch == "3":
        update_filme()

    elif switch == "4":
        list_filmes()

    elif switch == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")