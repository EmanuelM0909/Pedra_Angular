from time import sleep
c = ('\033[m',          # 0 - s/cor
     '\033[0;30;41m',   # 1 - vermelho
     '\033[7;30m',      # 2 - branco
     '\033[0;30;45m',   # 3 - roxo
     '\033[0;30;44m',   # 4 - azul
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[2], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)
    print(c[0], end='')
    sleep(1)

#programa principal
comando = ''
while True:
    titulo('SISTEMA de ajuda PyHELP', 1)
    comando = input("Função ou Biblioteca > ")
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo('FIM DO PROGRAMA!', 3)