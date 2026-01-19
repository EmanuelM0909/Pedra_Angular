#Crie um programa em Python que:
'''DESAFIO 2 — Controle + lógica (nível intermediário)
Crie um programa em Python que:
Pergunte nomes e idades de várias pessoas usando while True
Armazene os dados em uma lista
Cada pessoa deve ser representada por uma lista
Exemplo: ["Ana", 25]
O programa deve parar quando o nome for vazio ("")
No final, mostre:
Quantas pessoas foram cadastradas
A lista completa
O nome da pessoa mais velha
O nome da pessoa mais nova
A média das idades

 Regras (importante)
Use apenas o que você já aprendeu
Não usar funções ainda
Não usar dicionários
Tudo dentro de um único arquivo
Pode usar for, while, listas, if

 Dica (não é a solução)
Você vai precisar:
Um for para percorrer a lista no final
Variáveis auxiliares como:
maior_idade = 0
menor_idade = 0
Guardar também o nome junto da idade'''

pessoas = []

while True:
    nome = input("Digite o nome: ")

    if nome == "":
        break

    idade = int(input("Digite a idade: "))

    pessoa = [nome, idade]
    pessoas.append(pessoa)

# ------------------------------
# Verificação se alguém foi cadastrado
# ------------------------------
if len(pessoas) == 0:
    print("Nenhuma pessoa cadastrada.")
else:
    print(f"\nTotal de pessoas cadastradas: {len(pessoas)}")
    print("Lista completa:", pessoas)

    # Assume que a primeira pessoa é a mais velha e a mais nova
    nome_mais_velho = pessoas[0][0]
    maior_idade = pessoas[0][1]

    nome_mais_novo = pessoas[0][0]
    menor_idade = pessoas[0][1]

    soma_idades = 0

    for pessoa in pessoas:
        nome = pessoa[0]
        idade = pessoa[1]

        soma_idades += idade

        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho = nome

        if idade < menor_idade:
            menor_idade = idade
            nome_mais_novo = nome

    media = soma_idades / len(pessoas)

    print("Pessoa mais velha:", nome_mais_velho)
    print("Pessoa mais nova:", nome_mais_novo)
    print("Média das idades:", media)
