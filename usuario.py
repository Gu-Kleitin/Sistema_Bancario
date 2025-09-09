def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário (somente números): ")
    if not (cpf.isdigit() and len(cpf) == 11):
        print("CPF inválido! Digite exatamente 11 números.")
        return
    cpf = int(cpf)
    usuario = verificar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe um usuário com esse CPF!")
        return
    nome = input("Digite o nome completo: ")
    data_de_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})

    print("===== Usuário criado com sucesso! =====")


def verificar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None



class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class PessoaJuridica(Cliente):
    def __init__(self, nome_empresa, cnpj, endereco):
        super().__init__(endereco)
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        
