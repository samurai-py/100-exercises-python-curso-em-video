

contIdade = contHomem = contMulher20 = 0
texto = 'CADASTRE UMA PESSOA'
while True:
    print('-=' * 15)
    print('      CADASTRE UMA PESSOA')
    print('-=' * 15)
    idade = int(input('Insira a idade: '))
    if idade >= 18:
        contIdade += 1
    sexo = str(input('Insira o sexo: ')).upper().strip()
    while sexo not in 'MmFf':
        sexo = str(input('Insira o sexo: ')).upper().strip()
    if sexo == 'M':
        contHomem += 1
    if sexo == 'F' and idade < 20:
        contMulher20 += 1
    opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while opcao not in 'SN':
        print('-=' * 15)
        opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if opcao == 'N':
        break

print('FIM DO PROGRAMA!')
print(f'Ao todo, {contIdade} pessoas com mais de 18 anos foram registradas.')
print(f'Homens contabilizados: {contHomem}.')
print(f'Mulheres com menos de 20 anos contabilizadas: {contMulher20}')