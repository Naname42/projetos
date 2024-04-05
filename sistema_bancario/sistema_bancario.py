menu ='''
========================

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair 

========================
'''

saldo = 0
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu)

    if opcao == 'd':
        print ('Deposito')
        valor_deposito = float(input('Digite o valor desejado: '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Deposito R$ {valor_deposito:.2f}\n'
        else:
            print('Valor inválido')


    elif opcao == 's':

        
        if numero_saques < LIMITE_SAQUES:
            print('Saque')
            valor_saque = float(input('Digite o valor desejado: '))

            
            if valor_saque <= saldo and valor_saque > 0 and valor_saque <= 500:

                saldo -= valor_saque
                extrato += f'saque R$ {valor_saque:.2f}\n'
                numero_saques += 1

            elif valor_saque > 500:
                print('O valor solicitado ultrapassa o limite de saque de R$ 500.00 por operação')
            else:
                print (f'A conta não possui saldo suficiente\nO saldo atual é R$ {saldo:.2f}')
        else:
            print(f'Você excedeu o limite de saques diário')
       
    


    elif opcao == 'e':
        print('Extrato')
        print('As seguintes operaçãoes foram realizadas:')
        print('Nãou houveram movimentações' if not extrato else extrato)
        print(f'Seu saldo atual é R$ {saldo:.2f}')

    elif opcao == 'q':
        print('Sair')
        break
        
    
    else:
        print('Erro, opção inválida')
