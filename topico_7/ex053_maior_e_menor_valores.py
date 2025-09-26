resp = 'S'
media = soma = q = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
            if n < menor:
                menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / q
print(f'Você digitou {q} de números e a média é {media}.')
print(f'O maior foi {maior} e menor foi {menor}.')
