valor_inicial = float(input('Digite o valor inicial da dívida: R$'))
juros_mensal = float(input('Digite o juros mensal (%): '))
valor_pago = float(input('Digite o valor pago mensalmente: R$'))

mes = total_pago = total_juros = 0
while valor_inicial > 0:
    juros = valor_inicial * (juros_mensal / 100)
    valor_inicial += juros        # aumenta a dívida pelos juros
    total_juros += juros          # acumula quanto foi pago só de juros
    valor_inicial -= valor_pago   # agora subtrai o pagamento mensal
    total_pago += valor_pago      # soma ao total pago
    mes += 1

    # Para evitar números negativos no final
    if valor_inicial < 0:
        valor_inicial = 0

print('\n--- Resumo do Pagamento ---')
print(f'A dívida foi quitada em {mes} meses.')
print(f'Total pago: R${total_pago:.2f}')
print(f'Total de juros pagos: R${total_juros:.2f}')
