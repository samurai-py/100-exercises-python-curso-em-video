from random import randint

num = randint(0,99999999999999999999999999999999999999999999999999999999999999999999999)
print('O número sorteado foi', num)

if (num%2) == 0:
    print('O número é par')
else:
    print('O número é ímpar')

#RECEBENDO O NÚMERO:

numr = int(input('Digite um número inteiro: '))

if (numr%2) == 0:
    print('O número é par')
else:
    print('O número é ímpar')
