num = int(input('Mande um número inteiro: '))

print('Você escolheu o número: {}'.format(num))

base = int(input('Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nDigite 1, 2 ou 3: '))

if base == 1:
    print('Você escolheu a opção BINÁRIO.\nO número {} em BINÁRIO é: {}'.format(num, bin(num).lstrip('0b')))
elif base == 2:
    print('Você escolheu a opção OCTAL.\nO número {} em OCTAL é: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('Você escolheu a opção HEXADECIMAL.\nO número {} em HEXADECIMAL é: {}'.format(num, hex(num).lstrip('0x')))
else:
    print('Opção inválida, tente novamente.')