c = 0
cont = 0
soma = 0
while c != 999:
    c = int(input('Digite um valor: '))
    cont += 1
    if c != 999:
        soma += c
print('Fim')
print('Até a interrupção do programa, você digitou {} números.'.format(cont))
print('Com exceção do último número, a soma dos valores digitados foi {}'.format(soma))