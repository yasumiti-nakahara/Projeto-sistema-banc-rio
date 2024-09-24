def linhas():
    print('=-'*30)


saque = list()
deposito = list()
extrato = ''
saldo = 0
cont_saques = 1
choice = int
linhas()
print('Seja bem vindo!')
while True:
    choice = int(input('''Digite a opção desejada:
                       [ 1 ] Saque
                       [ 2 ] Depósito
                       [ 3 ] Extrato 
                       [ 4 ] Sair
                       OPÇÂO SELECIONADA: '''))
    if choice not in (1, 2, 3, 4):
        print('Opção inválida, tente novamente: ')
#Operação saque 
    if choice == 1:
        linhas()
        valor_saque = float(input('Digite o valor para ser sacado: R$'))
        if cont_saques <= 3:
            if valor_saque <= 500:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    cont_saques += 1
                    extrato += f"Saque: R${valor_saque:.2f}"
                    print(f'O saldo atualizado é de R${saldo:.2f}')
                else:
                    print('ERRO: Valor superior ao saldo')
            else:
                print('ERRO: Valor de saque ácima do limite permitido (R$500,00)')  
        else:
            print('ERRO: A quantidade de saques permitidos foi atingido')
        linhas()
#Operação Depósito                    
    if choice == 2:
        linhas()
        valor_depósito = float(input('Digite o valor à ser depositado: R$'))
        if valor_depósito > 0:
            saldo += valor_depósito
            print(f'O saldo atualizado é de R${saldo:.2f}')
            extrato += f'Depósito: R${valor_depósito:.2f}'
        else:
            print('ERRO: O valor digitado é inválido')
        linhas()
#Operação Extrato
    if choice == 3:
        linhas()
        print('\n         EXTRATO         ')
        print(f'Não foram realizadas transações.' if not extrato else extrato)
        print(f'\nSaldo final de R${saldo:.2f}')
        linhas()
#Operação finalização
    if choice == 4:
        linhas()
        print('VOLTE SEMPRE!')
        break
    