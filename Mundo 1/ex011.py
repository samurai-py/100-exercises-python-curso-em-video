altura = float(input('Insira a altura da parede: '))
largura = float(input('Insira a largura da parede: '))
area = altura * largura
tinta = area / 2

print('São necessários {:.1f}l de tinta para pintar uma parede com {}m² de área'.format(tinta,area))