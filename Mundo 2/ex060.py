num = int(input('Digite um número: '))
fatorial = 0
fator = num - 1
print(num, end=' x ')#prints do guanabara

while fator > 0:
    print('{}'.format(fator), end='')#prints do guanabara
    print(' x ' if fator > 1 else ' = ', end='')#prints do guanabara

    if fator == (num - 1):
        fatorial = num * fator
    if fator < (num - 1):
        fatorial = fatorial * fator
    fator -= 1

print(fatorial)

'''#Guanabara

n = int(input('Digite um número para calcular seu fatorial: '))
c = n #contador começa com nosso próprio número
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))'''

#Usando o módulo

'''from math import factorial

n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n,f))'''