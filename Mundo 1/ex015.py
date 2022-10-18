km = float(input('Quantos km você rodou com o carro? '))
dias = float(input('Por quantos dias o carro foi alugado? '))
kmValor = km * 0.15
diasValor = dias * 60
preco = dias + km

print('='*12,'RECIBO','='*12)
print('Dias alugados: {:.0f}, custando R$ {:.2f}'.format(dias, diasValor))
print('Quilômetros rodados: {:.2f}, custando R$ {:.2f}'.format(km, kmValor))
print('Total a pagar: R$ {:.2f}'.format(preco))
print('='*30)