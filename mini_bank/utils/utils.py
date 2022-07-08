import re
from ..ui import ui


def limpar_cpf(cpf):
    return re.sub(r'[^0-9]', '', cpf)


def validar_cpf(cpf: str):
    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not sequencia:
        return True
    
    return False


def is_float(valor: str):
    try:
        float(valor)
    except:
        return False
    else:
        return True
    

def tratar_valor_entrada(entrada):
    if entrada == '':
        return
    
    while not is_float(entrada):
        entrada = ui.valor_invalido()

    valor_deposito = float(entrada)
    if valor_deposito % 1 != 0:
        if not ui.continuar_sem_centavos(valor_deposito):
            return
            
    return valor_deposito // 1
