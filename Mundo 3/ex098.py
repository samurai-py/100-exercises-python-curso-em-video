from time import sleep
def lin():
    print('-='*30)


def contador(i, f, p):
    lin()
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f:
        for valor in range(i, f-1, -p):
            print(f'{valor} ', end='', flush=True)
            sleep(0.3)
        print('FIM!')
    if i < f:
        for valor in range(i, f+1, p):
            print(f'{valor} ', end='', flush=True)
            sleep(0.3)
        print('FIM!')


#Programa Principal
contador(1,10,1)
contador(10,0,2)
lin()
print('Agora é sua vez de personalizar a contagem: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

