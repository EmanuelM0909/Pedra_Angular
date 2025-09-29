count = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break           # sai do loop quando receber 999
    count += 1  # contador = contador + 1
    soma += count       # soma = soma + n
print(f"\nForam digitados {count} número(s) e a soma é {soma}.")
