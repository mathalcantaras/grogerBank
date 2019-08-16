print('Bem vindo ao sistema do banco fulano')

nome = input('Digite o seu nome ')
idade = int(input('Digite a sua idade '))
saldo = float(input('Digite o seu saldo '))
x = input(
      '\nDigite (1) para saque\n'
      'Digite (2) para depósito\n'
      'Digite (3) para empréstimo\n'
      'Digite (4) para vizualizar informações\n'
      'Digite (Qualquer outro texto ou número) para sair'
      )


def saque(saldo):
    valor_saque = float(input('Digite o valor do saque'))
    if valor_saque > 1000 and saldo < valor_saque:
        print('Não foi possível realizar o saque')
    else:
        print('Saque aprovado')
        saldo - valor_saque
        print('Saldo atual: {}'.format(saldo))


def deposito(saldo):
    valor_deposito = float(input('Digite o valor do deposito'))
    if valor_deposito > 5000:
        print('Depósito negado')
    else:
        saldo + valor_deposito
        print('Saldo atual: {}'.format(saldo))


def emprestimo(idade, saldo):
    if idade > 21 and saldo >= 1000:
        valor_emprestimo = float(input('Digite o valor do empréstimo'))

        if valor_emprestimo >= 2000 and valor_emprestimo < 15*saldo:
            saldo + valor_emprestimo
            print('Saldo atual: {}'.format(saldo))
    else:
        print('Empréstimo negado')


def vi_infos(nome, idade, saldo):
    print(nome)
    print(idade)
    print(saldo)


print('\nDigite (1) para saque\n'
      'Digite (2) para depósito\n'
      'Digite (3) para empréstimo\n'
      'Digite (4) para vizualizar informações\n'
      'Digite (Qualquer outro texto ou número) para sair'
      )

def infos(nome, saldo, idade):
    print(nome)
    print(saldo)
    print(idade)

if x is 1:
    print(saque)

elif x is 2:
    print(deposito)

elif x is 3:
    print(emprestimo)

elif x is 4:
    print(infos)

else:
    print('Obrigado por usar o sistema do banco')