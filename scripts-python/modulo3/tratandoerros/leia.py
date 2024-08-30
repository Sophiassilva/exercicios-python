def leiaFloat(msg):
    """
    Verifica se o dado recebido é um número real
    :param msg: mensagem para ser impressa ao usuário
    """
    while True:
        try:
            n = float(input(msg))
        except:
            print('ERRO. Digite um número real válido.')
            continue
        else:
            return n


def leiaInt(msg):
    """
    Verifica se o dado recebido é um número inteiro
    :param msg: mensagem para ser impressa ao usuário
    """
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO. Digite um número inteiro válido.')
            continue
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n1} e o número real {n2}.')
