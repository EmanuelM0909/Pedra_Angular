#exemplo de dicionário com estoque e operações de venda.
"""estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}
venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0
print("Vendas:\n ")
for op in venda:
    produto, quantidade = op
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo
print(f"Custo total: {total:21.2f}\n")
print(f"Estoque:\n")
for chave, dados in estoque.items():
    print(f"Descrição: ", chave)
    print(f"Quantidade: ", dados[0])
    print(f"Preço: , {dados[1]: 6.3f}\n")"""

estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}

total = 0

print("=== ESTOQUE INICIAL ===\n")
for chave, dados in estoque.items():
    print(f"{chave:10s} → {dados[0]} unidades — R$ {dados[1]:.2f}")
print("-=" * 30)

while True:
    produto = input("\nProduto (ou 'fim'): ").lower()

    if produto == 'fim':
        break

    if produto not in estoque:
        print("Produto não existe no estoque!")
        continue

    quantidade = int(input("Quantidade: "))

    if quantidade > estoque[produto][0]:
        print(f"Estoque insuficiente! Temos {estoque[produto][0]} unidades.")
        continue

    preco = estoque[produto][1]
    custo = preco * quantidade

    estoque[produto][0] -= quantidade
    total += custo

    print(f"✔ {quantidade} x {produto} vendidos → R$ {custo:.2f}")

print("\n" + "-=" * 30)
print(f" TOTAL DO CAIXA: R$ {total:.2f}")
print("-=" * 30)

print("\n=== ESTOQUE FINAL ===\n")
for chave, dados in estoque.items():
    print(f"{chave:10s} → {dados[0]} unidades — R$ {dados[1]:.2f}")
