'''import random

jkp = int(input('Escolha o que quer jogar:\n1 - Pedra\n2 - Papel\n3 - Tesoura\nJO-KEN-PO? '))

jogadas = [1, 2, 3]

jpc = random.choice(jogadas)

if jkp == jpc:
    print('Opa, nós dois jogamos a mesma opção, foi um empate rsrs'.format(jpc))
elif jkp == 1 and jpc == 2:
    print('O papel ganha da pedra, então eu venci :D')
elif jkp == 1 and jpc == 3:
    print('A pedra ganha da tesoura, então você venceu -_-')
elif jkp == 2 and jpc == 3:
    print('A tesoura ganha do papel, então eu venci :D')
elif jkp == 2 and jpc == 1:
    print('O papel ganha da pedra, então você venceu -_-')
elif jkp == 3 and jpc == 1:
    print('A pedra ganha da tesoura, então eu venci :D')
elif jkp == 3 and jpc == 2:
    print('A tesoura ganha do papel, então você venceu -_-')
else:
    print('Opção inválida, tente novamente')
print('-'*30)
print('Vamos jogar de novo? ¬u¬')
print('-'*30)'''

#Resolução do Master

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')