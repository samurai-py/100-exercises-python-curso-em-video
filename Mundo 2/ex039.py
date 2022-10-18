import datetime

ano = int(input('Em que ano você nasceu? '))

anoAtual = datetime.date.today().year

anoSaldo = anoAtual - ano


print('Sua idade:', anoSaldo)

if anoSaldo < 18:
    print('Ainda faltam {} anos para você se alistar'.format(18 - anoSaldo))
elif anoSaldo == 18:
    print('Esse é o ano do seu alistamento, boa sorte!')
elif anoSaldo > 18:
    print('Você está atrasado, seu ano de alistamento foi em {}'.format(ano + 18))

