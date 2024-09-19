from time import sleep

while True:
    print('\033[0;31;40mSISTEMA DE PESQUISA - BIBLIOTECAS PYTHON\033[m\n')
    bib = input('Digite o nome da biblioteca [digite "FIM" para sair]: ').strip().lower()
    sleep(1)
    if bib.upper() == 'FIM':
        break
    else:
        help(bib)