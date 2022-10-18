from random import randint

rand1 = (randint(1,99))
rand2 = (randint(1,99))
rand3 = (randint(1,99))
rand4 = (randint(1,99))
rand5 = (randint(1,99))

aleatorios = (rand1, rand2, rand3, rand4, rand5)
print(f'Os valores sorteados foram: {aleatorios[0]} {aleatorios[1]} {aleatorios[2]} {aleatorios[3]} {aleatorios[4]}')
print(f'O maior valor sorteado foi {sorted(aleatorios)[-1]}')
print(f'O menor valor sorteado foi {sorted(aleatorios)[0]}')

