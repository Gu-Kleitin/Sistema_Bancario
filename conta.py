from usuario import verificar_usuario
from datetime import datetime

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
    
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia):
        super().__init__(cliente, numero, agencia)
        self._limite = 3700
        self._limite_saques = 5
        self._numero_saques = 0
        #self._taxa_manutencao = 7.99
        #self._cheque_especial = 2000 serão implementados quando houver um banco de dados

class ContaPoupanca(Conta):
    def __init__(self, cliente, numero, agencia):
        super().__init__(cliente, numero, agencia)
        self._limite = 2500
        self._limite_saques = 3
        self._numero_saques = 0
        #self._rendimento = 0.05
        #self._data_rendimento = None serão implementados quando houver um banco de dados

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
