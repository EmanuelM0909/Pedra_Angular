produto = float(input('Qual o valor do produto: '))
print('Formas de pagamento:\n'
      '[1] - Dinheiro/Cheque\n'
      '[2] - Cartão avista.\n'
      '[3] - Cartão em até 2x sem juros.\n'
      '[4] - Cartão em até 3x com juros.')
forma_pg = int(input('Qual a forma de pagamento: '))
if forma_pg == 1:
    novo = produto - (produto * 10 / 100)
    print(f'O produto ficou de R${novo} com o desconto de 10% á vista!')
elif forma_pg == 2:
    novo = produto - (produto * 5 / 100)
    print(f'O produto ficou de R${novo} com o desconto de 5% á vista, no cartão!')
elif forma_pg == 3:
    novo = produto
    parcela = novo / 2
    print(f'Sua compra será parcelada em 2x de {parcela}.')
    print(f'O produto ficou com o preço normal. R${produto}!')
elif forma_pg == 4:
    novo = produto + (produto * 20 / 100)
    total_p = int(input('Quantas parcelas: '))
    parcela = novo / total_p
    print(f'Sua compra será parcelada em {total_p}` de {parcela}.')
    print(f'O produto ficou de R${novo} com o acréscimo de 20% em 3x no cartão!')
else:
    print("ERRO > Tente novamente!")
