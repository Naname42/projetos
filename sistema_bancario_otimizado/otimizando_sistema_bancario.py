def menu():

    menu ='''
    ========================

    [d] Deposito
    [s] Saque
    [e] Extrato
    [q] Sair 
    [ca] cadastro de usuário
    ========================
    '''
    return input(menu)


def cadastro_usuario(usuarios, cpf, nome, data_nascimento, logradouro, nro,  bairro, cidade, sigla_estado):

    novo_usuario = {'dados':{'cpf':cpf,'nome':nome,'data_nascimento':data_nascimento}, 'endereco':{'logradouro':logradouro,'nro':nro,'bairro':bairro,'cidade':cidade,'sigla_estado':sigla_estado}}
    usuarios.append(novo_usuario)
    
    return usuarios



#def abrir_conta()

def deposito (saldo,valor,extrato,/):
    if valor < 0:
        return print('Valor não reconhecido')
    else:
        saldo += valor
        extrato += f'Depósito no valor de R$ {valor:.2f}\n'

        return saldo, extrato
    
def saque (*,saldo,valor,extrato,limite,numero_saques,limite_saques):

    sem_saldo = valor > saldo
    sem_saque = numero_saques > limite_saques
    sem_limite = valor > limite

    if sem_saldo:
        print('Valor não disponivel para saque')
    elif sem_saque:
        print('Você excedeu o número máximo de saques por dia')
    elif sem_limite:
        print('Valor informado é maior que o limite por saque')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque no valor de R$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print('Saque falhou')
        
    return saldo,extrato
    
def exibir_extrato (saldo,/,*,extrato):

    print(f'As operações realizadas foram\n{extrato}')
    print(f'Seu saldo atual é de R$ {saldo:.2f}')

def main():

    saldo = 0
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    limite = 500
    usuarios = []

    while True:

        opcao = menu()

        if opcao =='d':
            valor = float(input('Insira o valor que deseja depositar:'))
            saldo, extrato = deposito(saldo,valor,extrato)

        elif opcao == 's':
            valor = float(input('Insira o valor que deseja sacar:'))

            saldo, extrato = saque(saldo = saldo,valor = valor,extrato = extrato,limite = limite,numero_saques = numero_saques,limite_saques = LIMITE_SAQUES)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato = extrato)

        elif opcao =='ca': #implementar o teste de CPF cadastrado
            cpf = input('Digite apenas os numeros do seu CPF: ')               
            nome = input('Digite seu nome: ')
            data_nascimento = input('Digite sua data de nascimento no formato dd/mm/aaaa: ')
            logradouro = input('Digite o nome da rua em que reside: ')
            nro = input('Digite o número e complemento: ')
            bairro = input('Digite o bairro: ')
            cidade = input('Digite o nome da sua cidade: ')
            sigla_estado = input('Digite a sigla de seu estado: ')                
            usuarios = cadastro_usuario(usuarios, cpf,nome,data_nascimento,logradouro,nro,bairro,cidade,sigla_estado)
            print('Usuario cadastrado com sucesso')
            
            print(usuarios)
             

        elif opcao == 'q':
            break

main()