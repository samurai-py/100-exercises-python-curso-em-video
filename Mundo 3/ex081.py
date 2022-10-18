valores = []
cont = cont5 0

while True:
    num = int(input('Digite um valor: '))
    cont += 1
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
valores.sort(reverse=True)
print(valores)
print(f'Você digitou {cont} números, mas apenas {len(valores)} valores foram adicionados.')
if 5 in valores:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')