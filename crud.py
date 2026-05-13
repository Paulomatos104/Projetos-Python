usuario = []

def new_usuario():
    nome = input("Digite o nome do usuário: ")
    usuario.append(nome)
    print("Usuário cadastrado com sucesso!")

def excluir_usuario():
    nome = input("Digite o nome do usuário a ser excluído: ")

    if nome in usuario:
        usuario.remove(nome)
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")

def update_usuario():
    nome = input("Digite o nome do usuário a ser atualizado: ")

    if nome in usuario:
        novo_nome = input("Digite o novo nome do usuário: ")
        index = usuario.index(nome)
        usuario[index] = novo_nome
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

def listar_usuario():
    print("\nUsuários cadastrados:")

    if len(usuario) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        for nome in usuario:
            print(nome)

# Menu principal
while True:
    print("\nBem-vindo ao sistema de gerenciamento de usuários!")
    print("Selecione uma opção:")
    print("1 - Cadastrar usuário")
    print("2 - Excluir usuário")
    print("3 - Atualizar usuário")
    print("4 - Listar usuários")
    print("5 - Sair")

    switch = input("Digite o número da opção desejada: ")

    if switch == "1":
        new_usuario()

    elif switch == "2":
        excluir_usuario()

    elif switch == "3":
        update_usuario()

    elif switch == "4":
        listar_usuario()

    elif switch == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")