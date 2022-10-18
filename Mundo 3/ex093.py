jogador = dict()
gols = list()
partidaGol = totalGol = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidaQtd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidaQtd):
    partidaGol = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(partidaGol)
    totalGol += partidaGol
jogador['gols'] = gols
jogador['total'] = totalGol #Tb pode se usar a função sum() na lista de partidas
print('-='*40)
print(jogador)
print('-='*40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*40)
print(f'O jogador {jogador["nome"]} jogou {partidaQtd} partidas.')
for i in range(0, partidaQtd):
    print(f'    => Na partida {i+1}, fez {jogador["gols"][i]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')