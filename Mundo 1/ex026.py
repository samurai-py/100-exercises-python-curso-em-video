frase = input('Escreva uma frase qualquer: ').upper().strip()

print("A letra 'a' aparece {} vezes na frase".format(frase.count('A')))
print("A letra 'a' aparece primeiro na {}ª posição".format(frase.find('A')+1))
print("A letra 'a' aparece por último na {}ª posição".format(frase.rfind('A')+1))