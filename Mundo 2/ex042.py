r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if (r1 <= r2 + r3) and (r2 <= r1 + r3) and (r3 <= r1 + r2):
    print('As três retas podem formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo é equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é isósceles!')
    else:
        print('O triângulo é escaleno!')
else:
    print('Essas três retas não conseguem formar um triângulo')