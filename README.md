# Sistema Bancário em Python

O projeto está sendo desenvolvido em Python utilizando recursos da linguagem para simular um sistema bancário simples, com foco em uma arquitetura mais modular e escalável.

## Funcionalidades
- **Depósito:** Permite adicionar dinheiro a uma conta específica.
- **Saque:** Permite retirar dinheiro de uma conta específica, com limite de valor e número de saques diários.
- **Extrato:** Exibe o histórico de transações e o saldo atual de uma conta.
- **Criação de Usuário:** Cria um novo usuário com base no CPF, nome, data de nascimento e endereço.
- **Criação de Conta:** Permite a criação de diferentes tipos de contas (Corrente e Poupança) vinculadas a um usuário existente.
- **Listar Contas:** Exibe todas as contas criadas no sistema.

## Estrutura do Projeto
O projeto utiliza a seguinte organização para separar as responsabilidades:

- `main.py`: Contém o menu principal e a lógica de interação com o usuário.
- `operacoes.py`: Reúne as funções de negócio (depósito, saque, extrato), mantendo-as separadas da interface do usuário.
- `usuario.py`: Lida com a lógica de criação e verificação de usuários.
- `conta.py`: Responsável pela criação e listagem de contas, além de definir os tipos de conta (Corrente e Poupança).

## Recursos Utilizados
- **Funções Modulares:** A lógica principal do programa é dividida em funções reutilizáveis em diferentes arquivos.
- **Listas e Dicionários:** Usadas para armazenar de forma organizada as informações de usuários e contas, permitindo que o sistema gerencie múltiplos usuários e contas de forma eficiente.
- **Constantes e Contadores por Conta:** O limite de saques e o número de saques realizados agora são atributos de cada conta, o que permite limites diferentes para cada tipo de conta.
- **Tratamento de Erros (`try/except`):** Garante que o programa não quebre ao lidar com entradas inválidas do usuário.

---

### Melhorias que já foram feitas:
- Criação de usuários e filtragem por CPF para evitar duplicidade.
- Diferentes tipos de contas (Corrente e Poupança).
- Lógica de saque e depósito refatorada para funcionar com contas específicas.
- Extrato agora é específico para cada conta, exibindo apenas as transações dela.

### Próximas melhorias planejadas:
- Guardar usuários e contas em um banco de dados ou planilha do Excel.
- Fazer transferência de valores entre contas de diferentes usuários.
