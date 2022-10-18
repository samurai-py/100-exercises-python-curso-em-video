'''lista = []
val = 0
par = []
impar = []
for i in range(0,7):
    val = int(input(f'Digite o {i+1}° valor: '))
    if (val%2) == 0:
        par.append(val)
    else:
        impar.append(val)

par.sort()
impar.sort()
lista.append(par)
lista.append(impar)

print(lista)'''


num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
