valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print('-='*30)
print('Você digitou os valores {}'.format(valores))
for v in valores:
    print(f'{v}...', end='')
print()
print(f'O maior valor foi {max(valores)}, e ele estava na(s) posição(es) ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c}... ', end='')

print(f'\nO menor valor foi {min(valores)}, e ele estava na(s) posição(es) ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c}... ', end='')

print('\nCheguei ao final da lista.')