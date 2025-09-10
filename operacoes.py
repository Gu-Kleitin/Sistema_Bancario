from datetime import datetime
from conta import Conta, ContaCorrente, ContaPoupanca

def depositar (conta, valor, /):
    if valor <= 0:
        raise ValueError("Valor do depósito deve ser positivo")
    conta.saldo += valor
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    conta.historico.append(f"{data_hora} - Depósito de R$ {valor:.2f}")
    return True

def sacar(*, conta, valor):

    if valor <= 0:
        raise ValueError("Valor do saque deve ser positivo")
    if valor > conta.limite:
        raise ValueError(f"Você não pode sacar mais do que R$ {conta.limite} por vez")
    if valor > conta.saldo:
        raise ValueError("Saldo insuficiente")
    conta.saldo -= valor
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    conta.historico.append(f"{data_hora} - Saque de R$ {valor:.2f}")
    return True

def mostrar_extrato(conta):
    print("\n========== EXTRATO ==========")
    for operacao in conta.historico:
        print(operacao)
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("=============================\n")

