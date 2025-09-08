num = int(input('Digite um número de 0 a 9999: '))

u = num % 10          # unidade
d = (num // 10) % 10  # dezena
c = (num // 100) % 10 # centena
m = (num // 1000) % 10 # milhar

print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
