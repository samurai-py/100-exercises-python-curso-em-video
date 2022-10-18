from datetime import date

anoAtual = date.today().year
cid = dict()
cid['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
ctps = int(input('Digite o registro da Carteira de Trabalho (0 Se não tiver): '))
cid['idade'] = anoAtual - ano
if ctps != 0:
    cid['ctps'] = ctps
    anoCont = int(input('Insira o ano de contratação: '))
    anoApos = (anoCont - ano) + 35
    cid['Ano de Contratação'] = anoCont
    cid['salário'] = float(input('Salário: R$ '))
    cid['Ano de Aposentadoria'] = anoApos
else:
    cid['ctps'] = 'Não tem'
print('-='*40)
for k, v in cid.items():
    print(f'O campo {k} tem o valor {v}')
