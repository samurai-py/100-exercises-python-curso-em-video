valores = []

while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar...')
    opcao = str(input('Você quer continuar? [S/N] ')).strip()
    while opcao not in 'SsNn':
        print('-=' * 15)
        opcao = str(input('Quer continuar? [S/N]: ')).strip()
    if opcao in 'Nn':
        break
valores.sort()
print(valores)



