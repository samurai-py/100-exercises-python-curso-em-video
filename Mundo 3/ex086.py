'''lista = []
val = []
for i in range(0,3):
    for p in range(0, 3):
        lista.append(int(input(f'Digite um valor para [{i}, {p}]: ')))'''



'''print('-='*50)
print(f'[{lista[0]: ^5}] [{lista[1]: ^5}] [{lista[2]: ^5}]')
print(f'[{lista[3]: ^5}] [{lista[4]: ^5}] [{lista[5]: ^5}]')
print(f'[{lista[6]: ^5}] [{lista[7]: ^5}] [{lista[8]: ^5}]')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()