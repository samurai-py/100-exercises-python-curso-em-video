lista = []
listaPar = []
listaImpar = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if (num%2) == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
    opcao = str(input('Você quer continuar? [S/N] ')).strip()
    while opcao not in 'SsNn':
        print('-=' * 15)
        opcao = str(input('Quer continuar? [S/N]: ')).strip()
    if opcao in 'Nn':
        break

listaPar.sort()
listaImpar.sort()
print(f'Os valores da lista original são {lista}')
print(f'Os valores pares da lista original são {listaPar}')
print(f'Os valores ímpares da lista original são {listaImpar}')