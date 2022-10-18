salario = float(input('Qual o valor do salário: '))
aum = (salario/100) * 15
salarioFinal = salario + aum

print('Com o aumento de 15%, o seu salário fica no total de R$ {:.2f}, apresentando um aumento de R$ {:.2f}'.format(salarioFinal, aum))