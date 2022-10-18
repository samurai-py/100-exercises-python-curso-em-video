import random
alu1 = input('Insira o nome do aluno 1: ')
alu2 = input('Insira o nome do aluno 2: ')
alu3 = input('Insira o nome do aluno 3: ')
alu4 = input('Insira o nome do aluno 4: ')
lista = alu1, alu2, alu3, alu4 #também dá pra transformar em uma lista []
sorteio = random.choice(lista)

print('O aluno sorteado foi o(a):', sorteio)

