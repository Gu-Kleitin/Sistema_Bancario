import saldo

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor de depósito: R$ "))
        try:
            novo_saldo = saldo.depositar(valor)
            saldo.extrato.append(f"Depósito de R$ {valor:.2f}")
        except ValueError as e:
            print(e)
    elif opcao == "2":
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saques:
            print("Número máximo de saques diários atingido.")
            continue
        else:
            valor = float(input("Informe o valor do saque: R$ "))
            try:
                novo_saldo = saldo.sacar(valor)
                saldo.extrato.append(f"Saque de R$ {valor:.2f}")
                numero_saques += 1
            except ValueError as e:
                print(e)
    elif opcao == "3":
        saldo.mostrar_extrato()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")