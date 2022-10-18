s = 0

for c in range(0,6):
    n = int(input('Digite um número: '))
    if (n % 2) == 0:
        s += n
        print(s)
    else:
        print('A soma ainda é:', s)
print('A soma total é:', s)