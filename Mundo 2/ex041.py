from datetime import date

ano = int(input('Em qual ano o atleta nasceu? '))

anoAtual = date.today().year

anoSaldo = anoAtual - ano

if anoSaldo <= 9:
    print('A categoria do atleta é: MIRIM')
elif anoSaldo <= 14:
    print('A categoria do atleta é: INFANTIL')
elif anoSaldo <= 19:
    print('A categoria do atleta é: JUNIOR')
elif anoSaldo == 20:
    print('A categoria do atleta é: SÊNIOR')
else:
    print('A categoria do atleta é: MASTER')