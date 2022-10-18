'''frase = input('Digite uma frase: ').upper().replace(' ', '')

print('O inverso de {} é {}'.format(frase,frase[::-1]))

if str(frase) == str(frase)[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')'''

#Resolução do Guanabara

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!!!')
else:
    print('A frase digitada não é um PALÍNDROMO!')