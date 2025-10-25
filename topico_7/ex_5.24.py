num = int(input('Digite quantos números primos você quer ver: '))

if num < 0:
    print('Número inválido. Digite um número > 0.')
else:
    if num >= 1:
        print('2')          # Primeiro primo
        cont = 1            # Já contamos 1 primo
        teste = 3           # Vamos testar a partir do 3

        while cont < num:   # Enquanto ainda faltar mostrar primos
            x = 3           # Primeiro divisor de teste
            while x < teste:      # Testa se há divisores até o número
                if teste % x == 0:
                    break        # Achou divisor → não é primo
                x += 2           # Próximo divisor ímpar
            if x == teste:       # Se chegou até ele mesmo → é primo!
                print(teste)
                cont += 1
            teste += 2           # Testa o próximo número ímpar
