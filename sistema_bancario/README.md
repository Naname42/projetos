# Sistema Bancário

Este projeto consistiu na criação de um sistema bancário simples. Não foram implementadas formas de acesso de usuário, concentrando-se apenas nas funcionalidades de depósitos, saques e extratos, conforme especificado a seguir:

* [Depósito](#depoisito)
* [Saque](#saque)
* [Extrato](#extrato)

### Considerações

Este projeto foi implementado de maneira simples e está incluído nos requisitos do bootcamp _**Coding The Future Vivo - Python AI Backend Developer**_. Embora eu já tivesse conhecimento prévio sobre o assunto, optei por não utilizar funções, já que esse conceito ainda não foi abordado no curso. Durante a execução do projeto, revisei muitas das operações básicas de Python, além das operações de Git, necessárias para a entrega do projeto.







## Depoisito

O depósito consiste em inserir um valor positivo em ponto flutuante que será adicionado ao saldo total. Além disso, o extrato deve conter uma descrição de todos os depósitos realizados.

## Saque

O saque envolve a subtração de um valor do saldo. Existe um limite de 3 operações de saque, com um valor máximo de R$ 500,00 por operação. Se o valor solicitado para saque exceder o saldo atual, uma mensagem de erro será exibida. Da mesma forma, mensagens personalizadas serão exibidas se o limite máximo por saque ou o limite de saques diários forem ultrapassados.

## Extrato

A operação de extrato deve informar todas as operações de saque e depósito efetuadas. Ao final das operações, o saldo final é exibido.

