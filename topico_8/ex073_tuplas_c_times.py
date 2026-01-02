t = ('Flamengo', 'Palmeiras', 'Palmeiras', 'Mirassol',
     'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio',
     'Red Bull Bragantino', 'Atlético-MG', 'Santos', 'Corinthians',
     'Vasco da Gama', 'Vitória', 'Internacional', 'Ceará',
     'Fortaleza', 'Fortaleza', 'Sport')
print('-=' * 30)
print('a)')
print(f'Os 5 primeiros são:\n {t[0:5]} ')
print('-=' * 30)
print('b)')
print(f'Os 4 ultimos são:\n {t[-4:]} ')
print('-=' * 30)
print('c)')
print('Ordem alfabética')
print(sorted(t))
print('-=' * 30)
print('d)')
print(f'O Ceará está em {t.index('Ceará')+1}')
print('-=' * 30)