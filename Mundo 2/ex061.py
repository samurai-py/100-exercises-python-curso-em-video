'''n = int(input('Digite um número: '))
r = int(input('Digite a razão da P.A.: '))
x = 10
ult = n + (x-1) * r
pa = n + r

print(n)
while pa <= ult:
    print(pa)
    pa += r'''


#Guanabara

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro #Dica, quando for começar a contar, fazer o Termo N ser igual ao valor inputado
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
