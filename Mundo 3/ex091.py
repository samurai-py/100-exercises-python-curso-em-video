#Solução parecida com a minha

'''from random import randint
from time import sleep

resultados = dict()
jogadores = list()
print('Valores sorteados:')
for i in range(1,5):
    n = randint(1,6)
    resultados[f'Jogador {i}'] = n
    jogadores.append(n)
    sleep(0.5)
    print(f'O Jogador{i} tirou {n}')
jogadores.sort(reverse=True)
jogar = 't'
print('Ranking dos jogadores:')
for p in range(0,4):
    print(f'{p+1}° lugar: ',end='')
    for k,v in resultados.items():
        if v == jogadores[p] and jogar != k:
            sleep(0.5)
            print(k,'com',v)
            jogar = k
            break'''

#Guanabara
from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list() #Antes era dict()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'    {k} tirou {v} no dado.')
    sleep(0.5)
sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
#print(ranking) Ao darmos print(ranking) a primeira vez, vemos que ele é apresentado como uma lista, então o tratamos como lista ou o convertemos para lista lá no início
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.5)























































'''jogo = dict()
tupladado = ()
listadado = []
lista = []
rank = dict()
print('Valores sorteados:')
for n in range(1,5):
    jogo['Jogador'] = f'Jogador{n}'
    jogo['dado'] = randint(1,6)
    print(f'    {jogo["Jogador"]} tirou {jogo["dado"]}')
    listadado.append(jogo['dado'])
    lista.append(jogo.copy())
    #sleep(0.5)
listadado.sort(reverse=True)
print(listadado)
print(lista)
print('Ranking dos jogadores:')

for i in range(0,4):
        if lista[i]['dado'] == listadado[i]:
            rank[f'{i}° Lugar'] = lista[i]
            print(rank[f'{i}° Lugar'])
            for k, v in lista[i].items():
                print(f'{i+1}° lugar: {k} com {v}')
print()'''


'''ranking = [(v, k) in k, v for jogo.items()]
ranking.sort(reverse=True)'''

