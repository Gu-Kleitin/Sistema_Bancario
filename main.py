import operacoes, usuario, conta

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Listar contas
[0] Sair
=> """

numero_saques = 0
LIMITE_SAQUES = 3 #tenho que olhar para implementar o limite que cada conta já tem
AGENCIA = "0001"
contas = []
usuarios = []


while True:
    opcao = input(menu)
    if opcao == "1":
        print("[1] Conta Corrente")
        print("[2] Conta Poupança")
        tipo = input("Escolha o tipo de conta que quer mexer: ")
        
        #Filtrando contas pelo tipo
        tipo_conta = "corrente" if tipo == "1" else "poupanca"
        contas_filtradas = [c for c in contas if c["tipo"] == tipo_conta]
        if not contas_filtradas:
            print("Nenhuma conta encontrada. Por favor, crie uma conta primeiro.")
            continue
        
        #selecionando a conta
        numero_conta = int(input("Informe o número da conta: "))
        try:
            numero_conta = int(numero_conta)
            conta_selecionada = None
            for c in contas_filtradas:
                if c["numero_conta"] == numero_conta:
                    conta_selecionada = c
                    break
            
            if conta_selecionada is None:
                print("Número de conta não encontrado para o tipo escolhido.")
                continue

        except (ValueError):
            print("Número de conta inválido. Deve ser um número inteiro.")
            continue

        #Realizando o depósito
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            conta_selecionada["saldo"] = operacoes.depositar(
                conta_selecionada["saldo"],
                valor,
                conta_selecionada["extrato"]
            )
            print("Depósito realizado com sucesso!")
        except ValueError as e:
            print(f"Erro ao depositar: {e}")

    elif opcao == "2":
        print("[1] Conta Corrente")
        print("[2] Conta Poupança")
        tipo = input("Escolha o tipo de conta que quer mexer: ")

        #Filtrando contas pelo tipo
        tipo_conta = "corrente" if tipo == "1" else "poupanca"
        contas_filtradas = [c for c in contas if c["tipo"] == tipo_conta]
        if not contas_filtradas:
            print("Nenhuma conta encontrada. Por favor, crie uma conta primeiro.")
            continue
        
        #selecionando a conta
        numero_conta = int(input("Informe o número da conta: "))
        try:
            numero_conta = int(numero_conta)
            conta_selecionada = None
            for c in contas_filtradas:
                if c["numero_conta"] == numero_conta:
                    conta_selecionada = c
                    break
            if conta_selecionada is None:
                print("Número de conta não encontrado para o tipo escolhido.")
                continue
        except (ValueError):
            print("Número de conta inválido. Deve ser um número inteiro.")
            continue

        #Realizando o saque
        try: 
            #Checando o limite de saques
            excedeu_saques = conta_selecionada["numero_saques"] >= conta_selecionada["limite_saques"]
            if excedeu_saques:
                print("Número máximo de saques diários atingido.")
                continue
            
            valor = float(input("Informe o valor do saque: R$ "))
            conta_selecionada["saldo"] = operacoes.sacar(
                saldo = conta_selecionada["saldo"],
                valor = valor,
                extrato = conta_selecionada["extrato"],
                limite = conta_selecionada["limite"],
                numero_saques = conta_selecionada["numero_saques"],
                limite_saques = conta_selecionada["limite_saques"],
            )
            conta_selecionada["numero_saques"] += 1 # Incrementa o número de saques
            print("Saque realizado com sucesso!")
        except ValueError as e:
            print(f"Erro ao sacar: {e}")


    elif opcao == "3":
        if not contas:
            print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
            continue
            
        numero_conta = int(input("Informe o número da conta para ver o extrato: "))
        conta_extrato = None
        for c in contas:
            if c["numero_conta"] == numero_conta:
                conta_extrato = c
                break
        
        if conta_extrato:
            operacoes.mostrar_extrato(conta_extrato["extrato"], conta_extrato["saldo"])
        else:
            print("Conta não encontrada.")

    elif opcao == "4":
        usuario.criar_usuario(usuarios)

    elif opcao == "5":
        print("[1] Conta Corrente")
        print("[2] Conta Poupança")
        tipo = input("Escolha o tipo de conta: ")
        numero_conta = len(contas) + 1  # Gera número de conta sequencial

        if tipo == "1":
            nova_conta = conta.conta_corrente(AGENCIA, numero_conta, usuarios)
        elif tipo == "2":
            nova_conta = conta.conta_poupanca(AGENCIA, numero_conta, usuarios)
        else:
            print("Tipo de conta inválido.")
            continue

        if nova_conta:
            contas.append(nova_conta)
            print("Conta criada e adicionada ao sistema!")
            print(f"Agência: {nova_conta['agencia']}")
            print(f"Número da conta: {nova_conta['numero_conta']}")
            print(f"Titular: {nova_conta['usuario']['nome']}")
        else:
            print("Falha ao criar conta.")

    elif opcao == "6":
        conta.listar_contas(contas)
          
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
