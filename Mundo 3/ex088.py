from random import randint
from time import sleep

temp = []
jogos = []
rand = 0


print('-'*50)
print('{: ^50}'.format('JOGA NA MEGA SENA'))
print('-'*50)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*7,'{: ^16}'.format(' SORTEANDO {} JOGOS'.format(qtd)),'-='*8)
for i in range(0, qtd):
    for p in range(0, 6):
        rand = randint(1, 61)
        if rand not in temp:
            temp.append(rand)
        temp.sort()
    jogos.append(temp[:])
    temp.clear()
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(0.5)

print('-='*8,'{: ^16}'.format(' < BOA SORTE! > '),'-='*8)


