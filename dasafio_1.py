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
        deposito = float(input("Informe o valor para deposito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito realizado de R$ {deposito:.2f}\n"
            print(f"Você depositou R$ {deposito:.2f} com sucesso!")
        else:
            print("Valor inválido.")
    
    elif opcao == "s":
        if numero_saques == LIMITE_SAQUES:
            print("Número máximo permitido para saques diários atingido.")
        
        else:
            print(f"Saldo disponível: R$ {saldo:.2f}")

            if saldo == 0:
                print("É preciso ter dinheiro em conta para poder realizar saques.")
            
            else:
                saque = float(input("\nInforme o valor para saque: "))

                if saque <= 0:
                    print("Valor inválido.")
                
                elif saque > limite:
                    print(f"Não é permitido sacar um valor superior à R$ {limite:.2f}.")
                
                elif saque > saldo:
                    print("Saldo insuficiente.")
                
                else:
                    saldo -= saque
                    extrato += f"Saque realizado de R$ {saque:.2f}\n"
                    numero_saques += 1
                    print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        
    
    elif opcao == "e":
        if extrato == "":
            print("Nenhuma movimentação foi realizada na sua conta ainda.")
        
        else:
            print("### Extrato ###")
            print(f"{extrato}")
            print(f"=> Saldo total: R$ {saldo:.2f}")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")