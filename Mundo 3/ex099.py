from time import sleep
def lin():
    print('-='*30)


def maior(*num):
    lin()
    print('Analisando os valores passados...')
    sleep(1.5)
    if num == ():
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')
    else:
        for valor in range(0, len(num)):
            print(f'{num[valor]} ', end='', flush=True)
            sleep(0.3)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
