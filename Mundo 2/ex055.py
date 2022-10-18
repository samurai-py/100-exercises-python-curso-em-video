'''peso = 0
ma = peso
me = peso

for i in range(1,6):
    peso = float(input('Insira o peso da {}ª pessoa: '.format(i)))
    me = peso
    if peso > ma:
        ma = peso
    elif peso < me:
        me = peso

print('O MAIOR número digitado foi {}.'.format(ma))
print('O MENOR número digitado foi {}.'.format(me))'''


#Guanabara

maior = 0
menor = 0

for p in range(1,6):
    peso = float(input('Insira o peso da {}ª pessoa: '.format(p)))
    if p == 1:    #Se estivermos analisando a primeira pessoa
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O MAIOR número digitado foi {}.'.format(maior))
print('O MENOR número digitado foi {}.'.format(menor))