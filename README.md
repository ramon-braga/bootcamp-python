# Banco DIO Bootcamp

## Descrição
Este projeto implementa um sistema bancário básico para completar o segundo desafio do Bootcamp de Python da DIO. Ele permite aos usuários realizar operações como depositar, sacar e exibir extratos em suas contas bancárias. Os usuários também podem criar novas contas, acessar contas existentes e visualizar suas contas. Diferenciando cada usuário por meio de login.

## Funcionalidades Principais

### 1. Operações Bancárias

- **depositar(saldo, valor, extrato):** Esta função permite ao usuário fazer um depósito em sua conta bancária. Recebe como entrada o saldo atual da conta, o valor a ser depositado e o extrato da conta. Retorna o novo saldo e o extrato atualizado.

- **sacar(\*, saldo, valor, extrato, limite, numero_saques):** Permite ao usuário realizar um saque em sua conta bancária. Verifica se o saldo é suficiente, se o valor do saque está dentro do limite diário permitido e se o número máximo de saques diários não foi ultrapassado. Retorna o novo saldo, o extrato atualizado e o número de saques realizados.

- **exibir_extrato(saldo, /, \*, extrato, nome, agencia, num_conta):** Exibe o extrato da conta bancária, incluindo detalhes como nome do cliente, número da agência e número da conta. Retorna o saldo atual e o extrato da conta.

### 2. Gerenciamento de Contas

- **menu_operacoes_em_conta(\*, cliente, conta):** Apresenta um menu de operações disponíveis para o usuário realizar em sua conta bancária, como depósito, saque, exibição de extrato e sair. Recebe como entrada o cliente e a conta em que as operações serão realizadas.

- **gera_num_conta():** Gera um número de conta bancária aleatório.

- **criar_conta(conta):** Cria uma nova conta bancária para o cliente, com um número de conta aleatório, número de agência fixo, saldo zero e extrato vazio. Retorna a lista de contas atualizada.

- **exibir_contas(cliente):** Exibe as contas bancárias associadas a um cliente específico, incluindo detalhes como número da agência, número da conta e saldo.

- **acessar_conta(cliente):** Permite ao usuário acessar uma conta bancária específica através do número da conta. Retorna o menu de operações em conta.

- **gerenciar_contas(cliente):** Apresenta um menu de opções para o usuário gerenciar suas contas bancárias, incluindo a criação de uma nova conta, acesso a uma conta existente e visualização das contas associadas ao cliente.

### 3. Autenticação e Cadastro

- **login(clientes):** Permite ao usuário fazer login no sistema bancário utilizando seu CPF. Retorna o menu de gerenciamento de contas.

- **valida_cpf(\*, cpf, clientes):** Verifica se um CPF está registrado entre os clientes existentes.

- **cadastrar(\*, clientes):** Permite cadastrar um novo usuário com uma nova conta bancária inserindo seus dados pessoais, incluindo CPF, nome, data de nascimento e endereço. Retorna a lista atualizada de clientes.

## Utilização

Para utilizar o código:

1. Execute o programa e escolha entre as opções de login, cadastro ou sair.
2. Ao optar por login, insira o CPF correspondente e siga as instruções apresentadas no menu. É necessário ter um cadastro para poder realizar login.
3. Ao optar por cadastro, insira seus dados pessoais conforme solicitado. O cadastro já incluirá uma conta por padrão, vinculada ao usuário.
4. Após fazer login você terá acesso às funcionalidades de gerenciamento de conta, onde poderá criar novas contas, acessar uma conta já existente para realizar operações bancárias disponíveis, tais como depositar, sacar e exibir extrato, além de poder visualizar todas as contas cadastradas no seu nome.

## Considerações Finais

Este código fornece uma estrutura básica para um sistema bancário simples, podendo ser expandido e melhorado conforme necessário.