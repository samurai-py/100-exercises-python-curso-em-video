from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opcao = int(input('Digite qualquer número para iniciar, 5 para encerrar: '))

while opcao != 5:
    print('-=' * 11)
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ]sair do programa')
    print('-=' * 11)
    opcao = int(input('Escolha uma opção: '))
    print('-=' * 11)
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print(n1 * n2)
    elif opcao == 3:
        if n1 > n2:
            print('{} é o maior'.format(n1))
        elif n1 < n2:
            print('{} é o maior'.format(n2))
        else:
            print('Os dois números são iguais')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida, tente novamente.')

print('Fim')

