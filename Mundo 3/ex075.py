n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

valores = (n1, n2, n3, n4)
print(f'Você digitou os valores {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if (valores.count(3)) >= 1:
    print(f'O número 3 apareceu na {valores.index(3)}ª posição')
elif (valores.count(3)) == 0:
    print(f'O número 3 não foi digitado em nenhuma posição')
print('Os números pares foram: ', end='')
for p in valores:
    if (p%2) == 0:
        print(p, end=' ')