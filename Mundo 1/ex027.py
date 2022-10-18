nome = input('Coloque seu nome completo: ').strip()

dividido = nome.split()
print('O primeiro nome é: {}\nE o último é: {}'.format(dividido[0],dividido[-1]))