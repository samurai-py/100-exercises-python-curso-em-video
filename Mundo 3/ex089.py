from time import sleep

turma = []
temp = []
aluno = []
media = []
nota1 = []
nota2 = []
notas = []
n1 = n2 = med = 0
op = 0

while True:
    aluno.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1 + n2) / 2
    nota1.append(n1)
    nota2.append(n2)
    media.append(med)
    notas.append(nota1[:])
    notas.append(nota2[:])
    nota1.clear()
    nota2.clear()
    temp.append(aluno[:])
    temp.append(media[:])
    temp.append(notas[:])
    aluno.clear()
    media.clear()
    notas.clear()
    turma.append(temp[:])
    temp.clear()
    opcao = str(input('Você quer continuar? [S/N] ')).strip()
    while opcao not in 'SsNn':
        print('-=' * 15)
        opcao = str(input('Quer continuar? [S/N]: ')).strip()
    if opcao in 'Nn':
        break
print('-='*40)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)

for p in range(0, len(turma)):
    print('{:<4}{:<10}{:>8}'.format(p, (turma[p][0][0]), (turma[p][1][0])))
print('-'*30)
while True:
    op = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if op <= (len(turma)-1):
        print(f'Notas de {turma[op][0][0]} são {turma[op][2]}')
        print('-' * 30)
    elif op >= 999:
        break
    else:
        print('OPÇÃO INVÁLIDA.', end= ' ')


print('FINALIZANDO...')
sleep(2)
print('<<< VOLTE SEMPRE >>>')
