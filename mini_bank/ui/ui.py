import os
from time import sleep
from ..utils import utils


def limpar_console():
    os.system('cls')
    
def console_input(monetario: bool = False):
    texto = '> '
    if monetario:
        texto += 'R$ '
    return input(texto).upper().strip()

def display_operacoes() -> None:
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato / Saldo")
    print("4 - Logout", end="\n\n")


def display_titulo(title: str) -> None:
    print("=" * 70)
    print("||", f"{title.upper():^66}", "||", sep="")
    print("=" * 70, end="\n\n")
    

def carregamento() -> None:
    sleep(0.35)
    print('.', end='', flush=True)
    sleep(0.35)
    print('.', end='', flush=True)
    sleep(0.35)
    print('.')
    sleep(0.2)


def finaliza_execucao() -> None:
    limpar_console()
    display_titulo('FINALIZANDO')
    print('Finalizando a execução', end='', flush=True)
    carregamento()
    

def operacao_invalida(titulo: str) -> None:
    limpar_console()
    display_titulo(titulo)
    print('Opção Inválida! Por favor escolha uma das opções abaixo:')
    display_operacoes()


def logout() -> None:
    limpar_console()
    display_titulo('LOGOUT')
    print('Fazendo logout', end='', flush=True)
    carregamento()


def solicitar_cpf(titulo: str) -> None:
    limpar_console()
    display_titulo(titulo)
    print(f'Bem vindo ao {titulo}!')
    print(' - Para continuar, insira seu CPF.')
    print(' - Para finalizar a execução, digite "X" ou "SAIR".', end='\n\n')


def cpf_invalido() -> None:
    print('CPF Inválido! Tente novamente.')


def display_menu_principal(titulo: str, nome_usuario: str, saldo: float) -> None:
    limpar_console()
    display_titulo(titulo)
    print(f"Olá, {nome_usuario}.")
    print(f"Saldo: R${saldo:.2f}\n")
    print("Por favor, escolha a operação desejada:")
    display_operacoes()


def deposito():
    limpar_console()
    display_titulo('DEPÓSITO')
    print('Insira o valor do depósito:')
    print(' - Deixe em branco para voltar ao menu principal')
    entrada = console_input(monetario=True)
    return utils.tratar_valor_entrada(entrada)


def saque(saldo_atual):
    limpar_console()
    display_titulo('SAQUE')
    print(f'Saldo Atual: R${saldo_atual:.2f}\n')
    print('Insira o valor para saque:')
    print(' - Deixe em branco para voltar ao menu principal\n')
    entrada = console_input(monetario=True)
    return utils.tratar_valor_entrada(entrada)


def valor_invalido():
    print('Valor inválido!')
    return console_input(monetario=True)


def continuar_sem_centavos(valor):
    print('O valor não pode conter centavos. A operação deve acontecer apenas com notas.')
    print(f'Deseja prosseguir com o valor de R${valor//1:.2f}? (S/N)')

    resposta = console_input()
    while resposta not in ("S", "N"):
        print('Opção Inválida!')
        resposta = console_input()

    return True if resposta == 'S' else False


def operacao_sucesso(operacao: str, saldo: float):
    limpar_console()
    display_titulo(operacao)
    print(f'{operacao} realizado com sucesso!')
    print(f'Novo saldo: R${saldo:.2f}')
    
    
def voltar_ao_menu_principal():
    print('\n1 - Voltar para o menu principal')
    print('2 - Logout')
    resposta = console_input()
    while resposta not in ('1', '2'):
        print('Opção Inválida!')
        resposta = console_input()
    return True if resposta == '1' else False
        
        
def saque_invalido():
    limpar_console()
    display_titulo('SAQUE')
    print('O valor solicitado para saque é maior que o saldo atual.')
    sleep(2)
    