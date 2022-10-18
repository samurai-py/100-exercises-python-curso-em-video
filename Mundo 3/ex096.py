def area(b, h):
    a = b * h
    print(f'A área de um terreno {h}x{b} é de {a}m².')


print()
print('Controle de Terrenos')
print('-'*30)
h = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(b, h)