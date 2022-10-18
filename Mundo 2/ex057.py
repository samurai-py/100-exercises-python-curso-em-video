sexo = '5'

while (sexo != 'M') and (sexo != 'F'):
    sexo = input('Insira o sexo da pessoa [ M / F ]: ').upper().strip()
    print(sexo)
print('Fim')

#Guanabara

sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))