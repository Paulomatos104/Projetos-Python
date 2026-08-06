import datetime
def decorador(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"[{datetime.datetime.now()}] Função '{func.__name__}' finalizada.")
        return resultado
    return wrapper

contas = []
transacoes = []

@decorador
def criar_conta():
    print("\n=== Criação de Conta ===")
    nome = input("Nome do titular: ")
    saldo_inicial = float(input("Saldo inicial: "))
    conta = {
        "nome": nome,
        "saldo": saldo_inicial
    }
    contas.append(conta)
    print("\nConta criada com sucesso!")

@decorador
def consultar_conta():  
    print("\n=== Consulta de Conta ===")
    nome = input("Nome do titular: ")
    for conta in contas:
        if conta["nome"] == nome:
            print(f"Titular: {conta['nome']}, Saldo: {conta['saldo']}")
            return
    print("Conta não encontrada.")

@decorador
def listar_contas():
    print("\n=== Listagem de Contas ===")
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(f"Titular: {conta['nome']}, Saldo: {conta['saldo']}")

@decorador
def depositar():
    print("\n=== Depósito ===")
    nome = input("Nome do titular: ")
    for conta in contas:
        if conta["nome"] == nome:
            valor = float(input("Valor do depósito: "))
            conta["saldo"] += valor
            transacoes.append(("depósito", nome, valor))
            print(f"Depósito de {valor} realizado com sucesso!")
            return

        
    print("Conta não encontrada.")

@decorador
def sacar():
    print("\n=== Saque ===")
    nome = input("Nome do titular: ")
    for conta in contas:
        if conta["nome"] == nome:
            valor = float(input("Valor do saque: "))
            if valor > conta["saldo"]:
                print("Saldo insuficiente.")
                return
            conta["saldo"] -= valor
            transacoes.append(("saque", nome, valor))
            print(f"Saque de {valor} realizado com sucesso!")
            return
    print("Conta não encontrada.")

@decorador
def transferir():
    print("\n=== Transferência ===")
    nome_origem = input("Nome do titular da conta de origem: ")
    nome_destino = input("Nome do titular da conta de destino: ")
    valor = float(input("Valor da transferência: "))
    
    conta_origem = None
    conta_destino = None
    
    for conta in contas:
        if conta["nome"] == nome_origem:
            conta_origem = conta
        if conta["nome"] == nome_destino:
            conta_destino = conta
            
    if not conta_origem:
        print("Conta de origem não encontrada.")
        return
    if not conta_destino:
        print("Conta de destino não encontrada.")
        return
    if valor > conta_origem["saldo"]:
        print("Saldo insuficiente na conta de origem.")
        return
    
    conta_origem["saldo"] -= valor
    conta_destino["saldo"] += valor
    transacoes.append(("transferência", nome_origem, nome_destino, valor))
    print(f"Transferência de {valor} realizada com sucesso!")

def listar_transacoes():
    print("\n=== Relatório de Transações ===")
    print("1 - Todas")
    print("2 - Depósitos")
    print("3 - Saques")
    print("4 - Transferências")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            filtro = None
        case "2":
            filtro = "depósito"
        case "3":
            filtro = "saque"
        case "4":
            filtro = "transferência"
        case _:
            print("Opção inválida.")
            return

    for transacao in transacoes:
        if filtro is None or transacao[0] == filtro:
            yield transacao
            
while True:

    print("""
=============================
 SISTEMA BANCÁRIO
=============================
1 - Cadastrar conta
2 - Listar contas
3 - Consultar conta
4 - Depósito
5 - Saque
6 - Transferência
7 - Relatório de transações
8 - Sair
=============================
""")

    match input("Escolha uma opção: "):
        case "1":
            criar_conta()

        case "2":
            listar_contas()

        case "3":
            consultar_conta()

        case "4":
            depositar()

        case "5":
            sacar()

        case "6":
            transferir()

        case "7":
            encontrou = False

            for transacao in listar_transacoes():
                encontrou = True

                if transacao[0] == "transferência":
                    tipo, origem, destino, valor = transacao
                    print(
                        f"Tipo: {tipo.title()} | "
                        f"Origem: {origem} | "
                        f"Destino: {destino} | "
                        f"Valor: R$ {valor:.2f}"
                    )
                else:
                    tipo, nome, valor = transacao
                    print(
                        f"Tipo: {tipo.title()} | "
                        f"Cliente: {nome} | "
                        f"Valor: R$ {valor:.2f}"
                    )
                if not encontrou:
                    print("Nenhuma transação encontrada.")

        case "8":
            print("\nEncerrando o sistema...")
            break

        case _:
            print("\nOpção inválida!")