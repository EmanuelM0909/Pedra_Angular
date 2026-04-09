from time import sleep
def linha():
    print("-" * 30)

def cont_1_10():
    print("Contagem de 1 até 10 de 1 em 1: ")
    for c in range(10):
        sleep(0.5)
        print(f"{c+1}", end=' ')
    print("Fim")

def cont_10_0_2():
    print("Contagem de 10 até 0 de 2 em dois:")
    for c in range(10, 1, -2):
        print(f"{c}", end=' ')
        sleep(0.5)

    print("Fim")

def cont():
    print("Agora é sua vez!")
    inicio = int(input("Inicio: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    print(f"Contando de {inicio} até {fim} de {passo}.")
    for cont_1 in range(inicio, fim + 1, passo):
        print(f"{cont_1}", end=' ')
        cont_1 += 1
        sleep(0.5)
    print("Fim")

linha()
cont_1_10()
linha()
cont_10_0_2()
linha()
cont()
linha()