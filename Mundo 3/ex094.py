from operator import itemgetter

dados = {}
pessoas = []
opcao = sexo = ''
idade = media = somaidade = 0

while True:
    dados['nome'] = str(input('Nome: ')).strip()
    sexo = str(input('Sexo [M/F]: ')).strip()
    while sexo not in 'MmFf':
        print('OPÇÃO INVÁLIDA.')
        sexo = str(input('Sexo [M/F]: ')).strip()
    dados['sexo'] = sexo
    #idade = int(input('Idade: '))
    #valide['idade'] = idade
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    opcao = input('Quer continuar? [S/N]: ')
    if opcao in 'Nn':
        break
print(pessoas)
print(f'{len(pessoas)} foram cadastradas.')
for c in range(0, len(pessoas)):
    somaidade += pessoas[c]['idade']
media = somaidade / len(pessoas)
print('A média de idade do grupo é de {:.2f} anos'.format(media))
print('As mulheres do grupo são: ', end='')
for m in range(0, len(pessoas)):
    if pessoas[m]['sexo'] in 'Ff':
        print(f'{pessoas[m]["nome"]}', end=' ')
print()
print('As pessoas da lista que possuem idade maior à idade media do grupo são: ')
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > media:
        print()
        print(f'nome = {pessoas[i]["nome"]}; sexo = {pessoas[i]["sexo"]}; idade = {pessoas[i]["idade"]}')
print('<< ENCERRADO >>')

