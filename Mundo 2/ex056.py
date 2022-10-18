nave = str(input('Qual o nome da nave? '))
trip = int(input('Qual o tamanho da tripulação? '))

s = 0
media = 0
maisvelho = 0
nomevelho = ''
mulher20 = 0
for c in range(1,trip+1):
    print('----- {}ª PESSOA ----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F] ')).upper().strip()
    s += idade
    if c == 1 and sexo == 'M':
        maisvelho = idade
        nomevelho = nome
    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
            mulher20 += 1

media = s / c
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho da tripulação é {}, com {} anos.'.format(nomevelho, maisvelho))
print('A tripulação tem {} mulheres com menos de 20 anos'.format(mulher20))






'''from datetime import date

anoAtual = date.today().year
sp = 0
si = 0
idade = 0
velho = idade
novo = idade
s = 0
media = 0
for c in range(1,5):
    nome = input('Qual o nome da {}ª pessoa? '.format(c))
    idade = int(input('Qual a idade da {}ª pessoa? '.format(c)))
    sexo = input('Qual o sexo da {}ª pessoa? (M / F) '.format(c)).upper()
    novo = idade
    s += idade
    media = s / c
    if sexo == 'M':
        if idade > velho:
            velho = nome
            print(velho)
        elif idade < novo:
            novo = idade
            print(novo)
    elif sexo == 'F':
        if idade < 20:
            si += 1
            print(si)
    else:
        print('OPÇÃO INVÁLIDA!')
print('A média de idade do grupo é de {} anos'.format(media))'''





