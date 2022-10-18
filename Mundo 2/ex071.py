saque = saqueRest = 0

print('-='*15)
print('             BBM')

while True:
    print('-=' * 15)
    saque = int(input('Digite o valor a ser sacado: '))
    print('-' * 30)
    while saque != 0:
        if (saque % 50) != 0:
            print(f'Total de {saque // 50} cédulas de R$50')
            saqueRest = saque % 50
            if saqueRest % 20 != 0:
                print(f'Total de {saqueRest // 20} cédulas de R$20')
                saqueRest = saqueRest % 20
                if saqueRest % 10 != 0:
                    print(f'Total de {saqueRest // 10} cédulas de R$10')
                    saqueRest = saqueRest % 10
                    print(f'Total de {saqueRest // 1} cédulas de R$1')
                    break
                else:
                    print(f'Total de {saqueRest // 10} cédulas de R$10')
                    break
            else:
                print(f'Total de {saqueRest // 20} cédulas de R$20')
                break
        else:
            print(f'Total de {saque // 50} cédulas de R$50')
            break
    opcao = str(input('Deseja fazer outra operação? [S/N]: ')).upper().strip()
    while opcao not in 'SN':
        print('-=' * 15)
        opcao = str(input('Deseja fazer outra operação? [S/N]: ')).upper().strip()
    if opcao == 'N':
        break
print('-'*15)
print('AGRADECEMOS A PREFERÊNCIA!')
