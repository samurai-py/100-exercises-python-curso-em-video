from random import randint
from time import sleep
def sorteia(lst):
    print('Sorteando 5 valores pares da lista: ', end='')
    for i in range(0, 5):
        lst.append(randint(1, 10))
        print(f'{lst[i]} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lst):
    s = 0
    for p in range(0, len(lst)):
        if (lst[p]%2) == 0:
            s += lst[p]
    print(f'Somando os valores pares de {lst}, temos {s}')


#Programa Principal
numeros = []
sorteia(numeros)
somaPar(numeros)
