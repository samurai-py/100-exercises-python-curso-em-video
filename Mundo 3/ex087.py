lista = []
val = []

somapar = soma3col = maior2lin = 0

for i in range(0, 3):
    for p in range(0, 3):
        lista.append(int(input(f'Digite um valor para [{i}, {p}]: ')))
        if (lista[len(lista)-1]%2) == 0:
            somapar += lista[len(lista)-1]
        if p == 2:
            soma3col += lista[len(lista)-1]
        if i == 1:
            maior2lin = lista[len(lista)-1]
            if lista[len(lista)-1] > maior2lin:
                maior2lin = lista[len(lista)-1]
print('-='*50)
print(f'[{lista[0]: ^5}] [{lista[1]: ^5}] [{lista[2]: ^5}]')
print(f'[{lista[3]: ^5}] [{lista[4]: ^5}] [{lista[5]: ^5}]')
print(f'[{lista[6]: ^5}] [{lista[7]: ^5}] [{lista[8]: ^5}]')
print('-='*50)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {soma3col}.')
print(f'O maior valor da segunda linha é {maior2lin}.')