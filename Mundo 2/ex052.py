'''n = int(input('Digite um número: '))

if (n % 2) == 0 and n != 2:
    print('Esse número não é primo')
elif (n % 3) == 0 and n != 3:
    print('Esse número não é primo')
elif (n % 5) == 0 and n != 5:
    print('Esse número não é primo')
elif (n % 7) == 0 and n != 7:
    print('Esse número não é primo')
else:
    print('Esse número é primo!')'''

#Resolução do Guanabara

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='') #marca o valor com a cor AZUL
        tot += 1 #Conta se o número é divisível ou não
    else:
        print('\033[31m', end='') #marca o valor com a cor VERMELHA
    print('{} '.format(c), end='') #mostrando os valores de C
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')