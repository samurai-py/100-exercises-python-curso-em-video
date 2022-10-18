'''n = int(input('Digite um número: '))
r = int(input('Digite a razão da P.A.: '))

termos = str(input('Por padrão, o programa mostrará a P.A. até o 10° termo. Você quer modificar esse valor? [ s / n ] ')).upper().strip()
if termos == 'S':
    x = -1
    while x != 0:
        x = int(input('Insira a nova quantidade de termos (0 encerra o programa): '))
        ult = n + (x - 1) * r
        pa = n + r
        while pa <= ult:
            if pa == n + r:
                print(n)
                pa += r
            elif pa > n + r:
                print(pa)
                pa += r
    print('FIM')
elif termos == 'N':
    x = 10
    ult = n + (x - 1) * r
    pa = n + r
    print(n)
    while pa <= ult:
        print(pa)
        pa += r
    print('FIM')
else:
    print('OPÇÃO INVÁLIDA, O PROGRAMA SERÁ ENCERRADO!')'''

'''n = int(input('Digite um número: '))
r = int(input('Digite a razão da P.A.: '))
p = n
c = 0

termos = str(input('Por padrão, o programa mostrará a P.A. até o 10° termo. Você quer modificar esse valor? [ s / n ] ')).upper().strip()
if termos == 'S':
    x = -1
    while c < x:
        x = int(input('Insira a nova quantidade de termos (0 encerra o programa): '))
        pa = n + r
        while pa <= ult:
            if pa == n + r:
                print(n)
                pa += r
            elif pa > n + r:
                print(pa)
                pa += r
    print('FIM')
elif termos == 'N':
    x = 10
    ult = n + (x - 1) * r
    pa = n + r
    print(n)
    while pa <= ult:
        print(pa)
        pa += r
    print('FIM')
else:
    print('OPÇÃO INVÁLIDA, O PROGRAMA SERÁ ENCERRADO!')'''

#Guana
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro #Dica, quando for começar a contar, fazer o Termo N ser igual ao valor inputado
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))