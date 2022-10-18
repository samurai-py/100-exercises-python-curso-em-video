valores = []
num = 0

for c in range(0,5):
    num = int(input('Digite um número: '))
    if c == 0:
        valores.append(num)
    elif c == 1:
        if num > valores[-1]:
            valores.append(num)
        elif num < valores[0]:
            valores.insert(0, num)
    elif c == 2:
        if num > valores[-1]:
            valores.append(num)
        elif valores[0] < num < valores[1]:
            valores.insert(1, num)
        elif num < valores[0]:
            valores.insert(0, num)
    elif c == 3:
        if num > valores[-1]:
            valores.append(num)
        elif valores[0] < num < valores[1]:
            valores.insert(1, num)
        elif valores[1] < num < valores[2]:
            valores.insert(2, num)
        elif num < valores[0]:
            valores.insert(0, num)
    elif c == 4:
        if num > valores[-1]:
            valores.append(num)
        elif valores[0] < num < valores[1]:
            valores.insert(1, num)
        elif valores[1] < num < valores[2]:
            valores.insert(2, num)
        elif valores[2] < num < valores[3]:
            valores.insert(3, num)
        elif num < valores[0]:
            valores.insert(0, num)

print(valores)