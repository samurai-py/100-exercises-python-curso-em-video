viagem = int(input('Qual a distância da viagem? (Em Km/h): '))

if viagem <= 200:
    band1 = viagem * 0.5
    print('O preço da sua passagem vai ser de R${:.2f}'.format(band1))
else:
    band2 = viagem * 0.45
    print('O preço da sua passagem vai ser de R${:.2f}'.format(band2))