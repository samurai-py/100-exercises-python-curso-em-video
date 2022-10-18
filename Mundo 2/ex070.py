contProduto1000 = total = precoBarato = cont = 0
precoBarato = 999**100


while True:
    produto = str(input('Qual o produto que você deseja comprar? ')).upper().strip()
    preco = float(input('Qual o preço do produto? '))
    total += preco
    if preco > 1000.0:
        contProduto1000 += 1
    if preco < precoBarato:
        barato = produto
        precoBarato = preco
    opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while opcao not in 'SN':
        print('-=' * 15)
        opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if opcao == 'N':
        break

print()
print('-'*15)
print(f'Valor total da compra R${total:.2f}')
print(f'Itens caros no seu carrinho: {contProduto1000}')
print(f'O produto mais barato do seu carrinho é: {barato}')