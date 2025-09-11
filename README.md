# Sistema Bancário em Python

O projeto está sendo desenvolvido em Python com base nos estudos do curso de python com a Suzano da plataforma DIO.
No momento, estou mudando a organização do projeto para orientação a objeto para aprofundar mais meus conhecimentos na linguagem.

## Funcionalidades
- **Depósito:** Permite adicionar dinheiro a uma conta específica.
- **Saque:** Permite retirar dinheiro de uma conta específica, com limite de valor e número de saques diários.
- **Extrato:** Exibe o histórico de transações e o saldo atual de uma conta.
- **Criação de Usuário:** Cria um novo usuário com base no CPF, nome, data de nascimento e endereço.
- **Criação de Conta:** Permite a criação de diferentes tipos de contas (Corrente e Poupança) vinculadas a um usuário existente.
- **Listar Contas:** Exibe todas as contas criadas no sistema.

---

### Melhorias que já foram feitas:
- Criação de usuários e filtragem por CPF para evitar duplicidade.
- Diferentes tipos de contas (Corrente e Poupança).
- Lógica de saque e depósito refatorada para funcionar com contas específicas.
- Extrato agora é específico para cada conta, exibindo apenas as transações dela.

### Próximas melhorias planejadas:
- Guardar usuários e contas em um banco de dados ou planilha do Excel.
- Fazer transferência de valores entre contas de diferentes usuários.
