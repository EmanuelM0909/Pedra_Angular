'''Exercício 12: Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no ínicio de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.'''

deposito_inicial = float(input('Valor inicial para deposito: R$'))
taxa = float(input('Taxa de juro mensal: '))
deposito_mensal = float(input(f'Deposito mensal fixo: R$'))
mes = 1
saldo = deposito_inicial
while mes <= 24:
    saldo += deposito_mensal
    saldo += saldo * (taxa / 100)
    print(f'Saldo após o mês {mes}: R${saldo:.2f}')
    mes += 1

total_depositado = deposito_inicial + (deposito_mensal * 24)
ganho_juros = saldo - total_depositado

print('===' * 12)
print(f'Saldo final após 24 meses: R${saldo:.2f}')
print(f'Total depositado: R${total_depositado:.2f}')
print(f'Ganho com juros: R${ganho_juros:.2f}')
print('===' * 12)
print(f'O ganho obtido com os juros foi de {saldo:.2f}')
