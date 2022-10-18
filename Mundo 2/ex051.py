'''n = int(input('Digite um número: '))
r = int(input('Digite a razão da P.A.: '))

for c in range(n-n,[0,10], r):
    c += n
    print(c)'''


n = int(input('Digite um número: '))
r = int(input('Digite a razão da P.A.: '))
x = 10
ult = n + (x-1) * r


for c in range(n, ult+1, r):
    print(c)

