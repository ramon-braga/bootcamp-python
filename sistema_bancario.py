def depositar(saldo, valor, extrato):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado de R$ {valor:.2f}\n"
        print(f"Você depositou R$ {valor:.2f} com sucesso!")
    else:
        print("Valor inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques):
  
    if saldo == 0:
        print("É preciso ter dinheiro em conta para poder realizar saques.")
            
    elif valor <= 0:
        print("Valor inválido.")
                
    elif valor > limite:
        print(f"Não é permitido sacar um valor superior à R$ {limite:.2f}.")
                
    elif valor > saldo:
        print("Saldo insuficiente.")
                
    else:
        saldo -= valor
        extrato += f"Saque realizado de R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, *, extrato):

    if extrato == "":
        print("Nenhuma movimentação foi realizada na sua conta ainda.")
        
    else:
        string_1 = "Extrato"
        print()
        print(" Extrato ".center(41, "="))
        print()
        print(f"{extrato}")
        print("-".center(41, "-"))
        print(f"=> Saldo total: R$ {saldo:.2f}")
        print("=".center(41, "="))

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para deposito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == "s":
        if numero_saques == LIMITE_SAQUES:
            print("Número máximo permitido para saques diários atingido.")
        
        else:
            print(f"Saldo disponível: R$ {saldo:.2f}")
            valor = float(input("\nInforme o valor para saque: "))

            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques)
        
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")