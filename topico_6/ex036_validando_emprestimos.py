from time import sleep

print('===' * 8)
print(' Bem Vindo ao Banco Fox! \n Sua melhor opção.')
print('===' * 8)

# Entrada de dados
valor_casa = float(input('Qual o valor da casa em oferta: R$'))
sleep(1)
salario = float(input('Qual o valor do seu salário: R$'))
sleep(1)
anos = int(input('Em quantos anos deseja quitar a casa: '))
sleep(1)

# Cálculos
meses = anos * 12
parcela = valor_casa / meses
limite = salario * 30 / 100

# Resultado
print(f'\nPara pagar uma casa de R${valor_casa:.2f} em {anos} anos ({meses} meses)')
print(f'A prestação mensal será de R${parcela:.2f}')

print('\nAnalisando sua proposta...')
sleep(2)

if parcela <= limite:
    print(' Empréstimo aprovado!!!')
else:
    print(' Empréstimo negado!!!')