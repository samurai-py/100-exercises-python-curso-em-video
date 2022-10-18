from time import sleep
from random import randint

num = numpc = soma = cont = 0



while True:
    opcao = int(input('Você quer ser impar (1) ou par? (2) '))
    if opcao == 1:
        print('Você escolheu ÍMPAR')
        sleep(1)
        print('1...')
        sleep(1)
        print('2...')
        sleep(1)
        print('3...')
        sleep(1)
        print('Vamos arrastar!')
        numpc = randint(0,10)
        num = int(input('Sua opção: '))
        soma = num + numpc
        if (soma%2) != 0:
            print(f'A soma dos dois números é {soma}, um número ímpar. VOCÊ GANHOU! ')
            cont += 1
        else:
            print(f'A soma dos dois números é {soma}, um número par. VOCÊ PERDEU! ')
            break
    elif opcao == 2:
        print('Você escolheu PAR')
        sleep(1)
        print('1...')
        sleep(1)
        print('2...')
        sleep(1)
        print('3...')
        sleep(1)
        print('Vamos arrastar!')
        numpc = randint(0, 10)
        int(input('Sua opção: '))
        soma = num + numpc
        if (soma % 2) == 0:
            print(f'A soma dos dois números é {soma}, um número par. VOCÊ GANHOU! ')
            cont += 1
        else:
            print(f'A soma dos dois números é {soma}, um número ímpar. VOCÊ PERDEU! ')
            break
    else:
        print('Opção inválida, tente novamente,')
if cont == 0:
    print('Você não me venceu nenhuma vez, que mané!')
else:
    print(f'Até ser derrotado, você me venceu {cont} vezes.')
print('FIM DE JOGO!')