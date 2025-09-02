from datetime import datetime

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        raise ValueError("Valor do depósito deve ser positivo")
    saldo += valor
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato.append(f"{data_hora} - Depósito de R$ {valor:.2f}")
    return saldo

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor <= 0:
        raise ValueError("Valor do saque deve ser positivo")
    if valor > limite:
        raise ValueError(f"Você não pode sacar mais do que R$ {limite} por vez")
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    saldo -= valor
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato.append(f"{data_hora} - Saque de R$ {valor:.2f}")
    return saldo

def mostrar_extrato(extrato, saldo):
    print("\n========== EXTRATO ==========")
    for operacao in extrato:
        print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================\n")
