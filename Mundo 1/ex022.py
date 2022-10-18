nome = input('Digite seu nome completo: ')

print(nome.upper())
print(nome.lower())

#Pergunta 3 - Método 1
letrasQtd = (len(nome)) - (nome.count(' '))
print(letrasQtd)

#Pergunta 3 - Método 2
dividido = nome.split()
junto = ''.join(dividido)
print(len(nome))
print(len(junto))

print(len(dividido[0]))