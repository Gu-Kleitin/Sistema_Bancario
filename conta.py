from usuario import *
from datetime import datetime

class Conta:
    def __init__(self, cliente, numero):
        self._cliente = cliente
        self._numero = numero
        self._agencia = "0001"  
        self._saldo = 0
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero, agencia):
        return cls(cliente, numero, agencia)
        
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def depositar (conta, valor, /):
        if valor <= 0:
            raise ValueError("Valor do depósito deve ser positivo")
        conta.saldo += valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        conta.historico.append(f"{data_hora} - Depósito de R$ {valor:.2f}")
        return True

    @classmethod
    def mostrar_extrato(self):
        print("\n========== EXTRATO ==========")
        for transacao in self.historico.transacoes:
            print(transacao)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("=============================\n")

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia):
        super().__init__(cliente, numero, agencia)
        self._limite = 3700
        self._limite_saques = 5
        self._numero_saques = 0
        #self._taxa_manutencao = 7.99
        #self._cheque_especial = 2000 serão implementados quando houver um banco de dados
    
    def sacar(self, valor):
        numero_saques = self._numero_saques
        limite_saques = self._limite_saques
        
        if numero_saques >= limite_saques:
            print("\nOperação falhou! Número máximo de saques atingido.")
            return False
            
        elif valor > self._limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {self._limite:.2f}")
            return False
        
        else:
            sucesso = super().sacar(valor)
            if sucesso:
                self._numero_saques += 1
            return sucesso

class ContaPoupanca(Conta):
    def __init__(self, cliente, numero, agencia):
        super().__init__(cliente, numero, agencia)
        self._limite = 2500
        self._limite_saques = 3
        self._numero_saques = 0
        #self._rendimento = 0.05
        #self._data_rendimento = None serão implementados quando houver um banco de dados
    
    def sacar(self, valor):
        numero_saques = self._numero_saques
        limite_saques = self._limite_saques
        
        if numero_saques >= limite_saques:
            print("\nOperação falhou! Número máximo de saques atingido.")
            return False
            
        elif valor > self._limite:
            print(f"\nOperação falhou! O valor do saque excede o limite de R$ {self._limite:.2f}")
            return False

        else:
            sucesso = super().sacar(valor)
            if sucesso:
                self._numero_saques += 1
            return sucesso

class Historico:
    def __init__(self):
        self._transacoes = []
        self._data_abertura = datetime.now()
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )

def criar_conta(agencia, numero_conta, usuarios):
    print("=== CADASTRO DE CONTA ===")
    opcao = input("Informe o tipo de usuário (1 - Pessoa Física, 2 - Pessoa Jurídica):")
    if opcao == "1":
        cpf = input("Digite o CPF do usuário (11111111111): ")
        if not (cpf.isdigit() and len(cpf) == 11):
            print("CPF inválido! Digite exatamente 11 números.")
            return
        cpf = int(cpf)
        usuario_existente = verificar_usuario(cpf, usuarios)
        if usuario_existente and isinstance(usuario_existente, PessoaFisica):
            return usuario_existente
        print("Usuário não encontrado ou não é uma Pessoa Física, impossível criar conta.")
        return None
    elif opcao == "2":
        cnpj = input("Digite o CNPJ do usuário (11111111111111): ")
        if not (cnpj.isdigit() and len(cnpj) == 14):
            print("CNPJ inválido! Digite exatamente 14 números.")
            return
        cnpj = int(cnpj)
        usuario_existente = verificar_usuario(cnpj, usuarios)
        if usuario_existente and isinstance(usuario_existente, PessoaJuridica):
            return usuario_existente
        print("Usuário não encontrado ou não é uma Pessoa Jurídica, impossível criar conta.")
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
    cliente = criar_conta(agencia, numero_conta, usuarios)
    if cliente:
        nova_conta = ContaCorrente(cliente=cliente, numero=numero_conta, agencia = agencia)
        cliente.adicionar_conta(nova_conta)
        return nova_conta

    return None

def conta_poupanca(agencia, numero_conta, usuarios):
    cliente = criar_conta(agencia, numero_conta, usuarios)
    if cliente:
        nova_conta = ContaPoupanca(cliente=cliente, numero=numero_conta, agencia = agencia)
        cliente.adicionar_conta(nova_conta)
        return nova_conta
    return None
        
def selecionar_conta(numero_conta, contas):
    for conta in contas:
        if conta.numero == numero_conta:
            return conta
    return None