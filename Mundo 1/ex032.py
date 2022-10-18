from datetime import date
ano = int(input('Qual o ano que você quer analisar? (Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

anob4 = (ano%4)
anob100 = (ano%100)
anob400 = (ano%400)

if (anob4 == 0) or (anob4 and anob100 and anob400 == 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

#ALEATORIO

from random import randint
anor = randint(0,2022)
print('O ano que o computador escolheu foi {}'.format(anor))

if (anor%4) == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

#pegar data do computador
