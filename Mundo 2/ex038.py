n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número é maior que o segundo')
elif n1 < n2:
    print('O segundo número é maior que o primeiro')
else:
    print('Não existe número maior, os dois números são iguais')