
dex = 10
c = 1
while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print(f'---------------------------')
    if tab > 0:
        while c <= dex:
            print(f'{tab} x {c} = {tab*c}')
            c += 1
        print(f'---------------------------')
        c = 1
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
