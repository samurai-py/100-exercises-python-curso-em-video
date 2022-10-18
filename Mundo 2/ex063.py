'''n = int(input('Indique quantos termos quer visualizar: '))
n2 = 0


while n != 0:
    n2 = 0+1 + n'''

cont = int(input('Indique quantos termos quer visualizar: '))
c = 1
n = 0
print(n)
n1 = n + 1
print(n1)
n2 = n1 + n
print(n2)
n3 = n2 + n1
print(n3)
n4 = n3 + n2
while c < cont:
    if c == 1:
        print(n4)
        c += 1
    elif c > 1:
        n = n1
        n1 = n2
        n2 = n3
        n3 = n4
        n4 = n3 + n2
        print(n4)
        c += 1

print('FIM')