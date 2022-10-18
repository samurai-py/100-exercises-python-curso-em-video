n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('VOCÊ ESTÁ REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('VOCÊ ESTÁ EM RECUPERAÇÃO!')
elif media >= 7.0:
    print('VOCÊ ESTÁ APROVADO!')