produto = float(input('Qual o preço do produto: R$ '))
desc = produto - (produto * 5 / 100)
print(f'O produto que custava R${produto}, agora com o desconto de 5% custa R%{desc:.2f}')
