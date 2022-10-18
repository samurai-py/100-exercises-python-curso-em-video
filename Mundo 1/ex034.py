salario = float(input('Quanto você ganha atualmente? '))

if salario > 1250:
    aum = salario * 0.10
    salarioTotal = salario + aum
    print('Você receberá um aumento de R${:.2f}, totalizando um salário de R${:.2f}'.format(aum, salarioTotal))
else:
    aum = salario * 0.15
    salarioTotal = salario + aum
    print('Você receberá um aumento de R${:.2f}, totalizando um salário de R${:.2f}'.format(aum, salarioTotal))