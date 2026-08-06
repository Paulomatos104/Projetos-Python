# Usuário logado
permissao = {
    "admin": True
}

# Lista que armazenará os usuários
usuarios = []

# Decorator para verificar se o usuário é administrador
def somente_admin(func):
    def wrapper(*args, **kwargs):
        if permissao["admin"]:
            return func(*args, **kwargs)
        else:
            print("\nAcesso negado. Apenas administradores podem executar esta função.")
    return wrapper

# criação de id
def gerar_id():
    id = 1

    while True:
        yield id
        id += 1

# ==========================
# CREATE
# ==========================

contador_id = gerar_id()

def create_usuario():
    print("\n=== Cadastro de Usuário ===")

    nome = input("Nome: ")
    

    tipo = input("Permissão (admin/usuario): ").lower()

    admin = True if tipo == "admin" else False

    usuarios.append({
        "id": next(contador_id),
        "nome": nome,
        "admin": admin
    })

    print("\nUsuário cadastrado com sucesso!")


# ==========================
# READ
# ==========================
def list_usuario():

    print("\n===== USUÁRIOS CADASTRADOS =====")

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(f"""
Nome : {usuario["nome"]}
ID   : {usuario["id"]}
Admin: {usuario["admin"]}
-------------------------
""")


# ==========================
# UPDATE
# ==========================
def update_usuario():

    nome = input("\nDigite o nome do usuário que deseja alterar: ")

    for usuario in usuarios:

        if usuario["nome"] == nome:

            novo_nome = input("Novo nome: ")

            usuario["nome"] = novo_nome

            print("\nUsuário atualizado com sucesso!")
            return

    print("\nUsuário não encontrado.")


# ==========================
# DELETE
# ==========================
@somente_admin
def delete_usuario():

    nome = input("\nDigite o nome do usuário que deseja excluir: ")

    for usuario in usuarios:

        if usuario["nome"] == nome:

            usuarios.remove(usuario)

            print("\nUsuário removido com sucesso!")
            return

    print("\nUsuário não encontrado.")


# ==========================
# ALTERAR PERMISSÃO
# ==========================
@somente_admin
def alterar_permissao():

    nome = input("\nDigite o nome do usuário: ")

    for usuario in usuarios:

        if usuario["nome"] == nome:

            nova = input("Nova permissão (admin/usuario): ").lower()

            usuario["admin"] = (nova == "admin")

            print("\nPermissão alterada com sucesso!")
            return

    print("\nUsuário não encontrado.")


# ==========================
# MENU
# ==========================
while True:

    print("""
=============================
 SISTEMA DE USUÁRIOS
=============================
1 - Cadastrar usuário
2 - Listar usuários
3 - Atualizar usuário
4 - Excluir usuário
5 - Alterar permissão
6 - Sair
=============================
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        create_usuario()

    elif opcao == "2":
        list_usuario()

    elif opcao == "3":
        update_usuario()

    elif opcao == "4":
        delete_usuario()

    elif opcao == "5":
        alterar_permissao()

    elif opcao == "6":
        print("\nEncerrando o sistema...")
        break

    else:
        print("\nOpção inválida!")