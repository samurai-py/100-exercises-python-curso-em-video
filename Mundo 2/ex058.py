'''import random
from time import sleep
numpc = random.randint(1,10) #Faz o computador adivinhar
num = int(input('Em qual número eu pensei? '))
numCont = 0
while numpc != num:
    num = int(input('Você errou, tente novamente: '))
    numCont += 1
print('Parabéns, você acertou, e só precisou de {} tentativas :D'.format(numCont+1))'''

#Guanabara

from random import randint
computador = randint(0,10)
print('Aqui é o seu computador... acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))