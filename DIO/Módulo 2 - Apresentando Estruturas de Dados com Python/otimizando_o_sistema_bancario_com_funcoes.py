import textwrap

def menu():
    menu = """\n
    ==============================   MENU  ============================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    [nu]\tNovo Usuario
    [nc]\tNova Conta
    [lc]\tLista de contas
    [q]\tSair
    ===================================================================
    => """
    return input(textwrap.dedent(menu))

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # Função de Saque
    
    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n@@@ Você não tem saldo suficiente. @@@")
        
    elif excedeu_limite:
        print("\n@@@ O valor do saque excede o limite. @@@")
        
    elif excedeu_saques:
        print("\n@@@ Número máximo de saques excedidos. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += (f"Saque: \t\tR$ {saque:.2f}\n")
        numero_saques += 1
        print("\n==== Saque realizado com sucesso! ====")
        print(f"\n==== Valor sacado: R$ {saque:.2f} ====")
        print(f"\n==== Saldo em conta: {saldo:.2f} ====")

    else:
        print("\n@@@ Valor inválido para saque. @@@")
    
    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    
    if deposito > 0:
        saldo += deposito
        extrato += (f"Depósito: \tR$ {deposito:.2f}\n")
        print(f"Valor depositado: R$ {deposito:.2f}")
        print(f"Saldo em conta: R$ {saldo:.2f}")

    else:
        print("Valor inválido para depósito.")

def extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO =========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: \tR$ {saldo:.2f}")
    print("==============================")

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente numeros): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('Ja existe usuario com esse CPF: ')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, N - bairro - cidade/ sigla estado)')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('==== Usuario registrado com sucesso ! ====')

def filtrar_usuarios(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta():
    cpf = input('informe o CPF do usuario: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\n Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\n Usuario não encontrado, fuluxo de criação de conta encerrado: ')
    return None

def listar_contas():

    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Tiitular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do deposito: '))
    
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                conta.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Opção invalida, por favor selicione novamente um opção válida.')

main()
