#Crie um programa em Python que:
""" Pergunte vários nomes ao usuário dentro de um while True. Cada nome digitado deve ser colocado em uma lista.
Se o usuário digitar vazio (“”), o programa deve parar. No final, o programa deve:
Mostrar quantos nomes foram digitados. >>> Mostrar todos os nomes na ordem que foram informados.
Mostrar os nomes em ordem alfabética. >>> Mostrar apenas o primeiro e o último nome digitado
Use: >>> while >>> break >>> listas >>> len() >>> sorted()"""

l = []
while True:
    nome = str(input("Digite um nome: "))

    if nome == '':
        print("Você não digitou nada")
        break

    l.append(nome)
print(f'Você cadastrou {len(l)} pessoas.')
print(f'Lista em ordem de cadastro: {l}')
print(f'Lista em ordem alfabética: {sorted(l)}')
if len(l) > 0:
    print("Primeiro:", l[0])
    print("Último:", l[-1])
else:
    print("Nenhum nome foi digitado")
