from abc import ABC,abstractmethod,abstractproperty
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento,endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Conta:
    def __init__(self,numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo    

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Operação falhou. Você não tem saldo suficiente')

        elif valor > 0:
            self._saldo -= valor
            print('Saque realizado com sucesso.')
            return True

        else:
            print ('Operação falhou. O valor informado é inválido')

        return False
    
    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
            print('Deposito realizado com sucesso')

        else:
            print('Operação falhoui. Valor informado é inválido')
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self,numero,cliente, limite=500, limite_saques=3):
        super().__init__(numero,cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self,valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]

        )
        excedeu_limite = valor >self._limite
        excedeu_saques = numero_saques >self._limite_saques

        if excedeu_limite:
            print('Operação falhou. O valor excede o limite.')

        elif excedeu_saques:
            print('Operação falhou. Número máximo de saques excedido')

        else:
            return super().sacar(valor)

        return False
    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente._nome}
         '''

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao (self,transacao):
        self._transacoes.append(
            {
                'tipo':transacao.__class__.__name__,
                'valor':transacao.valor,
            }
        )

class Transacao (ABC):

    @property
    @abstractproperty
    def registrar(self):
        pass

    @abstractmethod
    def registrar(self,conta):
        pass

class Deposito (Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

    def depositar(self,depositar):
        self._depositar = depositar

class Saque (Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

    def depositar(self,depositar):
        self._depositar = depositar

def menu():

    menu ='''
    ========================

    [d] Deposito
    [s] Saque
    [e] Extrato 
    [nu] Criar cliente
    [nc] Abir Conta
    [lc] Listar contas

    [q] SAIR
    ========================
    '''
    return input(menu)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('Cliente não possui conta')
        return  

    return cliente.contas[0] 

def depositar(clientes):
    cpf = input('Infirme CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não cadastrado')
        return
    
    valor = float(input('Informe o valor do depósico: '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta,transacao)

def sacar(clientes):
    cpf = input('Infirme CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não cadastrado')
        return
    
    valor = float(input('Informe o valor do depósico: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta,transacao)

def exibir_extrato(clientes):
    cpf = input('Infirme CPF do cliente')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não cadastrado')
        return 

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    print('Extrato:')
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        extrato = 'Não foi realizada nenhuma moviemntação'

    else:
        for transacao in transacoes:
            extrato += f'\n {transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}'

    print(extrato)
    print(f'Saldo\nR$ {conta.saldo:.2f}')

def criar_cliente(clientes):
    cpf = input('Informe CPF do cliente: ').strip()
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('CPF já cadastrado')
        return 
    
    nome = input('informe o nome completo: ')
    data_nascimento = input ('Informe a data de nascimento(dd-mm-aaaa): ')
    endereco = input('Informe o endereço(rua, número, bairro - cidade/sigla do estado): ')

    cliente = PessoaFisica(nome= nome, data_nascimento = data_nascimento, cpf = cpf, endereco = endereco)

    clientes.append(cliente)

    print('Cliente cadastrado com sucesso.')


def criar_conta(num_conta, clientes, contas):
    cpf = input('Informe CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado. Realize o cadastro de cliente antes de criar uma conta')
        return 

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=num_conta)
    contas.append(conta) 
    cliente.contas.append(conta)

    print('A conta foi criada.')


def listar_contas(contas):
    for conta in contas:
        print('=' * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            depositar(clientes)

        elif opcao =='s':
            sacar(clientes)

        elif opcao =='e':
            exibir_extrato(clientes)

        elif opcao =='nu':
            criar_cliente(clientes)

        elif opcao =='nc':
            numero_contas = len(contas) + 1
            criar_conta (numero_contas, clientes, contas)

        elif opcao =='lc':
            listar_contas(contas)

        elif opcao =='q':
            break
main()