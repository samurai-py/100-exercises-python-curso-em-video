casa = float(input('Qual o valor da casa que você quer financiar? '))
sal = float(input('Qual sua renda mensal? '))
prazo = int(input('Em quantos anos você pretente pagar? '))

prest = casa / (prazo*12)

porcrenda = prest / sal

print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa,prazo), end=' ')
print('o valor da prestação será de R${:.2f}'.format(prest))


if porcrenda <= 0.3:
    print('Seu empréstimo foi aprovado! Você terá que pagar parcelas de R${:.2f}, divididas em {} vezes.'.format(prest,(prazo*12)))
else:
    print('Seu empréstimo foi negado!')

