from random import randint

radar = randint(0, 220)

print('Limite de velocidade na rodovia: 80km/h\nSua velocidade: {}km/h'.format(radar))
if radar > 80:
    multa = (radar - 80) * 7
    print('Você ultrapassou o limite de velocidade')
    print('Sua multa custará R${:.2f}'.format(multa))
else:
    print('Você estava dentro do limite de velocidade.')

