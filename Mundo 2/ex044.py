preco = int(input('Qual o valor do produto? '))
op = int(input('Escolha a opção de pagamento:\n1 - À vista em dinheiro\cheque (10% de desconto)\n2 - À vista no cartão (5% de desconto)\n3 - 2x no cartão (Sem juros)\n4 - 3x ou mais no cartão (20% de juros)\nEscolha entre as opções 1, 2, 3 e 4: '))
precoFinal = 0

if op == 1:
    print('Você escolheu a opção: Pagamento à vista em dinheiro/cheque')
    precoFinal = preco - (preco*0.1)
elif op == 2:
    print('Você escolheu a opção: Pagamento à vista no cartão')
    precoFinal = preco - (preco*0.05)
elif op == 3:
    print('Você escolheu a opção: 2x no cartão')
    precoFinal = preco
elif op == 4:
    print('Você escolheu a opção: 3x ou mais no cartão')
    precoFinal = preco + (preco*0.2)
else:
    print('Opção inválida, tente novamente.')
print('O valor total da sua compra foi de R${:.2f}'.format(precoFinal))