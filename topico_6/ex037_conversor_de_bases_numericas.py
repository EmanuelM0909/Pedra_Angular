numero = int(input('Digite um número inteiro: '))
print('\033[33m[1]\033[m converter para BINÁRIO')
print('\033[33m[2]\033[m converter para OCTAL')
print('\033[33m[3]\033[m converter para HEXADECIMAL')
opcao = int(input('Sua opção é: '))

if opcao == 1:
    print(f'O número {numero} em BINÁRIO é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} em OCTAL é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O número {numero} em HEXADECIMAL é {hex(numero)[2:]}')
else:
    print('\033[7;31mERRO! Tente novamente!\033[m')