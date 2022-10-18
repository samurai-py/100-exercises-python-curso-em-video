import random
from time import sleep
numpc = random.randint(0,5) #Faz o computador adivinhar
num = int(input('Adivinhe o número que eu pensei (Entre 0 e 5): '))#Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if numpc == num:
    print('O número que eu pensei também foi {}, parabéns! :D'.format(numpc))
else:
    print('Você escolheu {}, mas o número que eu pensei foi {}, tente mais uma vez :('.format(num, numpc))