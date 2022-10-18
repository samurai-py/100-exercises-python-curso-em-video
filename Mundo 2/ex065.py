c = 0
cont = 0
soma = 0
media = 0
controle = 'S'
maior = 0
menor = 0
while controle == 'S':
    c = int(input('Digite um valor: '))
    cont += 1
    soma += c
    controle = str(input('Você deseja continuar? [ S/N ] ')).upper().strip()
    if cont == 1:
        menor = c
        maior = c
    elif cont > 1:
        if c > maior:
            maior = c
        elif c < menor:
            menor = c
media = soma / cont
print('Fim')
print('Você digitou {} números, e a média entre eles foi {}.'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))