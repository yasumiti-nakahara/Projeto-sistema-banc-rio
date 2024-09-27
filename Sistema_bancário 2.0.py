from datetime import datetime, date
import pytz

def linhas():
    print('=-'*30)

#Limitador de transações
def lim_transações(cont_transações):
    if cont_transações >= 10:
        print('ERRO: Limite de transações (10) atingido.')
        return True
    return False

#Operação Saque
def operação_saque(*, saldo, cont_saques, cont_transações, extrato):
    if lim_transações(cont_transações):
        return saldo, cont_saques, cont_transações, extrato
    
    linhas()
    valor_saque = int(input('Digite o valor a ser sacado:'))
    if cont_saques >= 3:
        print('ERRO: Limite de saques diários (3) atingido.')
    elif valor_saque > 500:
        print('ERRO: Valor de saque superior ao permitido (500).')
    elif valor_saque > saldo:
        print('Valor de salfo insulficiente.')
    else:
        saldo -= valor_saque
        cont_saques += 1
        cont_transações += 1
        extrato += f"Saque:\t\t R${valor_saque:.2f} ;{datetime.now(pytz.timezone("America/Sao_Paulo"))} \n"
        print(f'\nO saldo atualizado é de R${saldo:.2f}')
    linhas()
    return saldo, cont_saques, cont_transações, extrato

#Operação depósito
def operação_depósito(valor_deposito, saldo, cont_transações, extrato, /):
    if cont_transações(cont_transações):
        return saldo, cont_transações, extrato
    
    linhas()
    valor_deposito = int(input('Digite o valor a ser depositado: R$'))
    if valor_deposito < 0:
        print('ERRO: Valor digitado inválido.')
    else:
        saldo += valor_deposito
        cont_transações += 1
        print(f'O saldo atualizado é de R${saldo:.2f}')
        print()
        extrato += f'Depósito:\t\t R${valor_deposito:.2f} ; {datetime.now(pytz.timezone("America/Sao_Paulo"))}\n'
    linhas()
    return saldo, cont_transações, extrato

#Operação extrato
def operação_extrato(extrato, saldo):
    linhas()
    print('         EXTRATO         ')
    print(f'Não foram realizadas transações.' if not extrato else extrato)
    print(f'\nSaldo final de R${saldo:.2f}')
    linhas()

#cadastro de usuário
def cad_usuario(usuarios):
    linhas()
    print('CADASTRO DE USUÁRIO')
    linhas()
    cpf = input('Informe o seu CPF (SOMENTE números):')
    usuario = filtro_usuario(usuarios, cpf)

    if usuario:
        print('Usuário já cadastrado')
        linhas()
        return

    pessoas = {'nome' : '', 'data_nascimento' : '', 'cpf' : '', 'endereço': {'rua': '', 'n_casa' : '', 'bairro' : '', 'cidade_estado': ''}}
    pessoas['nome'] = str(input('Nome completo para cadastro:'))
    date_str = str(input('Data de nascimento [dd/mm/aaaa]: '))
    date_format = '%d/%m/%Y'
    pessoas['data_nascimento'] = datetime.strptime(date_str, date_format)
    pessoas['cpf'] = cpf
    linhas()
    print('CADASTRO DE ENDEREÇO')
    linhas()
    pessoas['endereço']['rua'] = str(input('Logradouro (rua/av.): '))
    pessoas['endereço']['n_casa'] = int(input('Número da casa: '))
    pessoas['endereço']['bairro'] = str(input('Bairro: '))
    pessoas['endereço']['cidade_estado'] = str(input('Cidade e estado(são paulo/SP): '))
    usuarios.append(pessoas.copy())
    return usuarios


#filto de usuario
def filtro_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None       

#cadastro de conta
def cad_conta(agencia, num_conta, usuarios):
    linhas()
    cpf = input('Digite o CPF do usuario: ')
    usuario = filtro_usuario(usuarios, cpf)

    if usuario:
        linhas()
        print('Conta criada com sucesso!')
        linhas()
        return{'agencia':agencia, 'num_conta':num_conta, 'usuarios':usuarios}
    print('Usuário não encontrado')
    linhas()

#Código principal
txt = "Seja bem vindo!"
linhas()
print(f'{txt:^60}')
linhas()
extrato = ''
saldo = 0
cont_saques = 0
cont_transações = 0
usuarios = []
contas = []
AGENCIA = '0001'
while True:
    choice = int(input(f'''
Digite a opção desejada:
[ 1 ] Saque
[ 2 ] Depósito
[ 3 ] Extrato 
[ 4 ] Cadastro de novo usário
[ 5 ] Abertura de nova conta
[ 6 ] Sair
OPÇÂO SELECIONADA: '''))
    if choice not in (1, 2, 3, 4, 5, 6):
        print('Opção inválida, tente novamente: ')
    elif choice == 1:
        saldo, cont_saques, cont_transações, extrato = operação_saque(saldo, cont_saques, cont_transações, extrato)
    elif choice == 2:
        saldo, cont_transações, extrato = operação_depósito(saldo, cont_transações, extrato)
    elif choice == 3:
        extrato, saldo = operação_extrato(extrato, saldo)
    elif choice == 4:
        cad_usuario(usuarios)
    elif choice == 5:
        num_conta = len(contas) + 1
        conta = cad_conta(AGENCIA, num_conta, usuarios)
        if conta:
            contas.append(conta)
        
    else:
        linhas()
        print('Muito obrigado!')
        linhas()
        break
