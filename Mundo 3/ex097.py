def escreva(txt):
    print('~'*(len(txt)+4))
    print(f'{txt:^{len(txt)+4}}')
    print('~'*(len(txt)+4))


#Programa Principal
escreva('Olá, Mundo!')