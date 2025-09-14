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

def verificar_usuario(documento, usuarios):
    for usuario in usuarios:
        if isinstance(usuario, PessoaFisica) and usuario.cpf == documento:
            return usuario
        elif isinstance(usuario, PessoaJuridica) and usuario.cnpj == documento:
            return usuario
    return None

def criar_usuario(usuarios):
    opcao = input("Informe o tipo de usuário a ser criado (1 - Pessoa Física, 2 - Pessoa Jurídica): ")  
    if opcao == "1":
        cpf = input("Digite o CPF do usuário (somente números): ")
        if not (cpf.isdigit() and len(cpf) == 11):
            print("CPF inválido! Digite exatamente 11 números.")
            return None
        cpf = int(cpf)
        usuario_existente = verificar_usuario(cpf, usuarios)
        if usuario_existente:
            print("Já existe um usuário com esse CPF!")
            return None
        nome = input("Digite o nome completo: ")
        data_de_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        novo_usuario = PessoaFisica(nome=nome, data_nascimento=data_de_nascimento, cpf=cpf, endereco=endereco)
        usuarios.append(novo_usuario)
        print("===== Usuário criado com sucesso! =====")
        return novo_usuario
    
    elif opcao == "2":
        cnpj = input("Digite o CNPJ do usuário (somente números): ")
        if not (cnpj.isdigit() and len(cnpj) == 14):
            print("CNPJ inválido! Digite exatamente 14 números.")
            return
        cnpj = int(cnpj)
        usuario_existente = verificar_usuario(cnpj, usuarios)
        if usuario_existente:
            print("Já existe um usuário com esse CNPJ!")
            return
        nome_empresa = input("Digite o nome da empresa: ")
        endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        novo_usuario = PessoaJuridica(nome_empresa=nome_empresa, cnpj=cnpj, endereco=endereco)
        usuarios.append(novo_usuario)

        print("===== Usuário criado com sucesso! =====")
