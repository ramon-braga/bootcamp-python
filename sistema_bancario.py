import random

# Funções

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        print(f"\n---> Você depositou R$ {valor:.2f} com sucesso!")
    else:
        print("\n---> Valor inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques):
  
    if saldo == 0:
        print("\n---> É preciso ter dinheiro em conta para poder realizar saques.")
            
    elif valor <= 0:
        print("\n---> Valor inválido.")
                
    elif valor > limite:
        print(f"\n---> Não é permitido sacar um valor superior à R$ {limite:.2f}.")
                
    elif valor > saldo:
        print("\n---> Saldo insuficiente.")
                
    else:
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\n---> Saque de R$ {valor:.2f} realizado com sucesso!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato, nome, agencia, num_conta):

    if extrato == "":
        print("\n---> Nenhuma movimentação foi realizada na sua conta ainda.")
        
    else:
        print()
        print(" Extrato ".center(41, "="))
        print(f"Cliente: {nome}")
        print(f"Agência: {agencia}")
        print(f"Número da conta: {num_conta}")
        print("-".center(41, "-"))
        print()
        print(f"{extrato}")
        print("-".center(41, "-"))
        print(f"=> Saldo total: R$ {saldo:.2f}")
        print("=".center(41, "="))

def menu_operacoes_em_conta(*, cliente, conta):

    menu = f"""

    {cliente["nome"]},
    você está na conta de número: {conta["num_conta"]}

    Qual operação deseja realizar?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    saldo = conta["saldo"]
    limite = 500
    extrato = conta["extrato"]
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor para deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

            conta["saldo"] = saldo
            conta["extrato"] = extrato
        
        elif opcao == "s":
            if numero_saques == LIMITE_SAQUES:
                print("\n---> Número máximo permitido para saques diários atingido.")
            
            else:
                print(f"Saldo disponível: R$ {saldo:.2f}")
                valor = float(input("\nInforme o valor para saque: "))

                saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques
                )

                conta["saldo"] = saldo
                conta["extrato"] = extrato
            
        elif opcao == "e":

            exibir_extrato(
                saldo,
                extrato=extrato,
                nome=cliente["nome"],
                agencia=conta["agencia"],
                num_conta=conta["num_conta"]
            )
        
        elif opcao == "q":
            break

        else:
            print("\n---> Operação inválida, por favor selecione novamente a operação desejada.")

def gera_num_conta():
    num_gerado = random.randint(100, 999)
    return num_gerado

def criar_conta(conta):

    # cada conta criada possui um número de conta aleatório,
    # um número de agência fixo, saldo em zero e extrato vazio.

    num_conta = gera_num_conta()

    conta.append(
        { "num_conta": num_conta, "agencia": "0001", "saldo": 0, "extrato": "" }
    )
    return conta

def exibir_contas(cliente):
    contas = ""

    for conta in cliente["contas"]:
        contas += f"Número da agência: {conta["agencia"]}\n"
        contas += f"Número da conta: {conta["num_conta"]}\n"
        contas += f"Saldo: R$ {conta["saldo"]:.2f}\n"
        contas += f"{"-".center(41, "-")}\n"
    
    print("=".center(41, "="))
    print(f"Cliente: {cliente["nome"]}")
    print(f"CPF: {cliente["cpf"]}")
    print(f"{"=".center(41, "=")}")
    print(contas)

def acessar_conta(cliente):
    num_conta = int(input("Informe o número da conta: "))
    nao_encontrou = True
    
    for conta in cliente["contas"]:
        if conta["num_conta"] == num_conta:
            nao_encontrou = False
            menu_operacoes_em_conta(cliente=cliente, conta=conta)
    
    if nao_encontrou:
        print("\n---> Número de conta inválido.")

def gerenciar_contas(cliente):
    menu = f"""
    === Gerencie suas contas ===

    Olá, {cliente["nome"]},
    como deseja prosseguir?
    
    1. Criar nova conta
    2. Acessar conta corrente
    3. Visualizar contas
    0. Sair
    
    ==> """

    while True:
        opcao = int(input(menu))

        if opcao == 1:
            criar_conta(cliente["contas"])
            print("\n---> Conta criada com sucesso!")

        elif opcao == 2:
            acessar_conta(cliente)
        
        elif opcao == 3:
            exibir_contas(cliente=cliente)
        
        elif opcao == 0:
            break

        else:
            print("\n---> Opção inválida.")
    
def login(clientes):
    cpf = int(input("Informe seu CPF: "))
    nao_encontrou = True

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            nao_encontrou = False
            gerenciar_contas(cliente)
    
    if nao_encontrou:
        print("\n---> CPF não encontrado.")

def valida_cpf(*, cpf, clientes):
    eh_cliente = False

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            eh_cliente = True
    
    return eh_cliente

def cadastrar(*, clientes):

    cpf = int(input("CPF: "))

    # se o CPF já existir, o cadastro deve ser interrompido e retornar None
    if valida_cpf(cpf=cpf, clientes=clientes):
        return
    
    else:
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        logadouro = input("Logadouro: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        uf = input("UF: ")

        conta = []
        
        # por padrão cada cliente começa com uma conta zerada
        clientes.append(
            {
                "cpf": cpf,
                "nome": nome,
                "data_nascimento": data_nascimento,
                "endereco": {
                    "logadouro": logadouro,
                    "bairro": bairro,
                    "cidade": cidade,
                    "uf": uf
                },
                "contas": criar_conta(conta)
            }
        )

    return clientes

# Início do programa

menu = """
    =================
        Banco DIO
    =================

    1. Login
    2. Cadastrar
    0. Sair

==> """

clientes = []

while True:
    opcao = int(input(menu))

    if opcao == 1:
        login(clientes)
        
    elif opcao == 2:

        cadastrado = cadastrar(clientes=clientes)

        if cadastrado:
            clientes = cadastrado
        
        else:
            print("\n---> Este CPF já é cadastrado.")

    elif opcao == 0:
        break

    else:
        print("\n---> Opção inválida.")