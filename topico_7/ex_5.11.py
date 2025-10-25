'''Exercício 11: Escreva um program que pergunte o déposito inicial e  a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. escreva o total ganho com juros no período.'''

deposito = float(input("Valor do depósito inicial (R$): "))
taxa_percent = float(input("Taxa de juros mensal (%): "))
taxa = taxa_percent / 100.0
mes = 1
saldo = deposito
ganho_total = 0.0
while mes <= 24:
    juros_mes = saldo * taxa
    saldo += juros_mes
    ganho_total += juros_mes
    print(f'Mês {mes:2d}: Juros = R${juros_mes:.2f}  Saldo = R${saldo:.2f}')
    mes += 1
print("\nResumo após 24 meses:")
print(f"Saldo final: R${saldo:.2f}")
print(f"Ganho total com juros: R${ganho_total:.2f}")
