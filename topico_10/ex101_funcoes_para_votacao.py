def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos, não vota.'
    elif idade <= 16 or 18 or idade > 65:
        return f"Com {idade} anos, vota se quiser"
    else:
        return f"Com {idade} anos, voto obrigatorio."

nasc = int(input("Diga o ano de nascimento: "))
print(voto(nasc))
