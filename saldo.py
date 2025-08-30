saldo = 0
extrato = []

def depositar(valor):
    global saldo
    if valor <= 0:
        raise ValueError("Valor do depósito deve ser positivo")
    saldo += valor
    return saldo

def sacar(valor):
    global saldo
    if valor <= 0:
        raise ValueError("Valor do saque deve ser positivo")
    if valor > 500:
        raise ValueError("Você não pode sacar mais do que R$ 500 por vez")
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    saldo -= valor
    return saldo

def mostrar_extrato():
    print("\n========== EXTRATO ==========")
    for operacao in extrato:
        print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================\n")