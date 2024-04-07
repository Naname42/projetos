# Sistema Bancário otimizado

Este projeto foi a atualização do projeto de sistema bancario simples, em que o código fonte foi refeito para um padrão de funções. Além disso, foram implementadas as funções de criação de usuário e de criação de conta.

* [Depósito](#depoisito)
* [Saque](#saque)
* [Extrato](#extrato)
* [Criação de usuário](#criação-de-usuário)
* [Criação de conta](#criação-de-conta)


### Considerações

Este projeto foi implementado de maneira simples e está incluído nos requisitos do bootcamp _**Coding The Future Vivo - Python AI Backend Developer**_. 

## Depoisito

O depósito consiste em inserir um valor positivo em ponto flutuante que será adicionado ao saldo total. Além disso, o extrato deve conter uma descrição de todos os depósitos realizados.

## Saque

O saque envolve a subtração de um valor do saldo. Existe um limite de 3 operações de saque, com um valor máximo de R$ 500,00 por operação. Se o valor solicitado para saque exceder o saldo atual, uma mensagem de erro será exibida. Da mesma forma, mensagens personalizadas serão exibidas se o limite máximo por saque ou o limite de saques diários forem ultrapassados.

## Extrato

A operação de extrato deve informar todas as operações de saque e depósito efetuadas. Ao final das operações, o saldo final é exibido.

## Criação de usuário

Esta função adiquiri informações sobre o usuário e às armazena dentro de um dicionário que é adicionado dentro de uma lista. Só pode haver um usuário para cada CPF.

## Criação de conta

Para criar uma conta é necessário informar um cpf de um usuário já cadastrado. O cpf, o numero da conta e a agência são incluidas dentro de uma lista de dicionárioos. É possível criar mais de uma conta por cpf, porém as contas tem um numero único. Este número foi implementado a partir da conta (função len()) do numero de dicionários dentro da lista. Esta solução foi incluida para não utilizar uma variavel do tipo global, para que sejam mantidas as boas práticas.