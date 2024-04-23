# Sistema Bancário 3 (orientado a objetos)

Este projeto foi a atualização do projeto de sistema bancario 2 (funções), em que o código fonte foi refeito para o paradigma de orientação a objetos. Além disso, foi implementada a função de listar as contas associadas ao cliente.

* [Depósito](#depoisito)
* [Saque](#saque)
* [Extrato](#extrato)
* [Criação de usuário](#criação-de-usuário)
* [Criação de conta](#criação-de-conta)


### Considerações

Este projeto está incluído nos requisitos do bootcamp _**Coding The Future Vivo - Python AI Backend Developer**_. 
Provou ser um desafio significativo de implementar, principalmente porque a programação orientada a objetos era um conceito novo para mim. Dediquei várias horas tentando implementá-lo sozinho, mas eventualmente percebi a necessidade de revisar o projeto com a ajuda de videoaulas para otimizar o código. Para melhor compreensão do funcionamento do código, realizei uma série de testes com prints, os quais posteriormente foram removidos. Além disso, busquei esclarecimentos e sugestões por meio de mentorias.

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