def leiaInt(msg):
    """
    Verifica se o dado recebido é um número inteiro
    :param msg: mensagem para ser impressa ao usuário
    """
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print('ERRO! Digite um número inteiro válido!')


num = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {num}.')
