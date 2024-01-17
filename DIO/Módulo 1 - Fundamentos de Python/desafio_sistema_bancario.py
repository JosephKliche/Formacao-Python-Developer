menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print("Escolha a operação desejada:")
    opcao = input(menu)

    if opcao == "1":    #operação de depósito
        print("Depósito")

        deposito = float(input("Informe o valor desejado para depósito: ")) #local que o usuário informará o valor que será depositado
        
        if deposito > 0:
            saldo += deposito
            extrato += (f"Depósito: R$ {deposito:.2f}\n")
            print(f"Valor depositado: R$ {deposito:.2f}")
            print(f"Saldo em conta: R$ {saldo:.2f}")

        else:
            print("Valor inválido para depósito.")
    
    elif opcao == "2":  #operação de saque
        print("Saque")

        saque = float(input("Informe o valor desejado para saque: ")) #local que o usuário informará o valor que será sacado

        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Número máximo de saques excedidos")

        elif saque > 0:
            saldo -= saque
            extrato += (f"Saque: R$ {saque:.2f}\n")
            print(f"Valor sacado: R$ {saque:.2f}")
            print(f"Saldo em conta: {saldo:.2f}")

        else:
            print("Valor inválido para saque.")


    elif opcao == "3":  #operação de extrato
    
        print("\n========== EXTRATO =========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "4":  #saída do sistema
        break

    else:   #essa é parte que informa o erro, caso seja escolhida uma opção inexistente
        print("Operação inválida. Por favor, selecione novamente a opção desejada.")