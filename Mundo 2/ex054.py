from datetime import date

anoAtual = date.today().year
sp = 0
si = 0

for i in range(1,8):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(i)))
    if (anoAtual - ano) >= 21:
        sp += 1
        print(sp)
    else:
        si += 1
        print(si)
print('''O número de pessoas maiores de idade é {} e o de pessoas menores de idade é {}.'''.format(sp,si))
