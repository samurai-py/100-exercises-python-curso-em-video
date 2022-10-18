'''galera = list()
dado = list()
listaLeve = []
listaPeso = []
totpeso = totleve = cont = cont2 = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    galera.append(dado[:])
    dado.clear()  # Se não botar clear, os valide vão se acumular na lista
    cont += 1
    opcao = str(input('Você quer continuar? [S/N] ')).strip()
    while opcao not in 'SsNn':
        print('-=' * 15)
        opcao = str(input('Quer continuar? [S/N]: ')).strip()
    if opcao in 'Nn':
        break

for p in galera:
    cont2 += 1
    if cont2 == 1:
        totleve = p[1]
        listaLeve.append(p[0])
        totpeso = p[1]
        listaPeso.append(p[0])
    if cont2 > 1:
        if p[1] < totleve:
            listaLeve.clear()
            totleve = p[1]
            listaLeve.append(p[0])
        elif p[1] == totleve:
            listaLeve.append(p[0])
        elif p[1] > totpeso:
            listaPeso.clear()
            totpeso = p[1]
            listaPeso.append(p[0])
        elif p[1] == totpeso:
            listaPeso.append(p[0])

print('-='*50)
print(f'{cont} pessoas foram cadastradas:\n{galera}')
print(f'A lista das pessoas mais pesadas são {listaPeso}')
print(f'A lista das pessoas mais leves são {listaLeve}')'''

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:       #usando o len como contador
        mai = men = temp[1]     #Dando o valor do peso
    else:
        if temp[1] > mai:   #O temp[1] pode ser provisório, mas as variáveis mai e men, não.
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()


