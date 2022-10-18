paren1 = []
paren2 = []
c = 0

exp = str(input('Digite uma expressão: '))
while c < len(exp):
    if exp[c] == '(':
        paren1.append(c)
    elif exp[c] == ')':
        paren2.append(c)
    c += 1
if (len(paren1)) == (len(paren2)):
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')