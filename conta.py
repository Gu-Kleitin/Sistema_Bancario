from usuario import verificar_usuario

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário (11111111111): ")
    if not (cpf.isdigit() and len(cpf) == 11):
        print("CPF inválido! Digite exatamente 11 números.")
        return
    cpf = int(cpf)
    usuario = verificar_usuario(cpf, usuarios)
    if usuario:
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado, impossível criar conta sem usuário.")
    return None

def listar_contas(contas):
    for conta in contas:
        lista = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(lista)

def conta_corrente(agencia, numero_conta, usuarios):
    conta = criar_conta(agencia, numero_conta, usuarios)
    if conta:
        conta["tipo"] = "corrente"
        conta["limite"] = 3700
        conta["limite_saques"] = 5
        #conta["limite_transferencias"] = 10
        conta["saldo"] = 0
        conta["extrato"] = []
        conta["numero_saques"] = 0
        #conta["taxa_manutencao"] = 7.99
        #conta[cheque_especial"] = 2000

    return conta

def conta_poupanca(agencia, numero_conta, usuarios):
    conta = criar_conta(agencia, numero_conta, usuarios)
    if conta:
        conta["tipo"] = "poupanca"
        conta["limite"] = 2500
        conta["limite_saques"] = 3
        #conta["limite_transferencias"] = 5
        conta["saldo"] = 0
        conta["extrato"] = []
        conta["numero_saques"] = 0
        #conta["cheque_especial"] = 1000
        #conta["rendimento"] = 0.05
        #conta["data_rendimento"] = None
        
    return conta
        
        