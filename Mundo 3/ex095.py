time = []
jogador = dict()
gols = list()
partidaGol = totalGol = 0
while True:
    print('-'*30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidaQtd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidaQtd):
        partidaGol = int(input(f'Quantos gols na partida {c+1}? '))
        gols.append(partidaGol)
        totalGol += partidaGol
    jogador['gols'] = gols[:]
    jogador['total'] = totalGol
    time.append(jogador.copy())
    opcao = input('Quer continuar? [S/N]: ')
    partidaGol = totalGol = 0
    gols.clear()
    if opcao in 'Nn':
        break
print('-='*40)
print(time)
print('-='*40)
print(f'{"cod":<4}{"nome":<10}{"gols":>8}{"total":>8}')
print('-'*30)
for p in range(0, len(time)):
    print(f'{p:<4}{str(time[p]["nome"]):<14}{str(time[p]["gols"])}{str(time[p]["total"]):>5}') #Listas e Dicionarios não podem ser modificados em fstrings, por isso precisam ser convertidos para str na visualização.
while True:
    print('-' * 30)
    dados = int(input('Mostrar valide de qual jogador? '))
    while (len(time)) <= dados < 999:
        print('OPÇÃO INVÁLIDA.')
        print('-' * 30)
        dados = int(input('Mostrar valide de qual jogador? '))
    if dados >= 999:
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[dados]["nome"]}:')
        for i in range(0, len(time[dados]["gols"])):
            print(f'    => Na partida {i+1}, fez {time[dados]["gols"][i]} gols.')

print('Fim')
