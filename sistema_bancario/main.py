import usuario as usuario, conta as conta
from transacao import Deposito, Saque

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Listar contas
[0] Sair
=> """

AGENCIA = "0001"
contas = []
usuarios = []

while True:
    opcao = input(menu)
    if opcao == "1":
        numero_conta = int(input("Informe o número da conta: "))
        conta_selecionada = conta.selecionar_conta(numero_conta, contas)
        if conta_selecionada:
            valor = float(input("Informe o valor do depósito: "))
            deposito = Deposito(valor)
            deposito.registrar(conta_selecionada)
        else:
            print("Conta não encontrada.")

    elif opcao == "2":
        numero_conta = int(input("Informe o número da conta: "))
        conta_selecionada = conta.selecionar_conta(numero_conta, contas)
        if conta_selecionada:
            valor = float(input("Informe o valor do saque: "))
            saque = Saque(valor)
            saque.registrar(conta_selecionada)
        else:
            print("Conta não encontrada.")

    elif opcao == "3":
        numero_conta = int(input("Informe o número da conta: "))
        conta_selecionada = conta.selecionar_conta(numero_conta, contas)
        if conta_selecionada:
            conta_selecionada.mostrar_extrato()
        else:
            print("Conta não encontrada.")

    elif opcao == "4":
        usuario.criar_usuario(usuarios)

    elif opcao == "5":
        print("[1] Conta Corrente")
        print("[2] Conta Poupança")
        tipo = input("Escolha o tipo de conta: ")
        numero_conta = len(contas) + 1  # Gera número de conta sequencial
        nova_conta = None

        if tipo == "1":
            nova_conta = conta.conta_corrente(usuarios, numero_conta, AGENCIA)
        elif tipo == "2":
            nova_conta = conta.conta_poupanca(AGENCIA, numero_conta, usuarios)
        else:
            print("Tipo de conta inválido.")
            continue

        if nova_conta:
            contas.append(nova_conta)
            print("Conta criada e adicionada ao sistema!")
            print(f"Agência: {nova_conta.agencia}")
            print(f"Número da conta: {nova_conta.numero}")
            print(f"Titular: {nova_conta.cliente.nome}")
        else:
            print("Falha ao criar conta.")

    elif opcao == "6":
        for c in contas:
            print("=" * 50)
            print(f"Agência: {c.agencia}")
            print(f"C/C: {c.numero}")
            print(f"Titular: {c.cliente.nome}")
          
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")