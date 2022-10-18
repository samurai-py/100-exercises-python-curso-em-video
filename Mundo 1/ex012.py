preco = float(input('Qual o preço do produto: '))
desc = (preco/100) * 5
precoFinal = preco - desc

print('Com o desconto de 5%, o produto desejado fica com o valor de R$ {:.2f}, economizando um total de R$ {:.2f}'.format(precoFinal, desc))