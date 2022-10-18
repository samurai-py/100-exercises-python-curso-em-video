import math

x = float(input('Coloque o valor do cateto oposto: '))
y = float(input('Coloque o valor do cateto adjacente: '))
hip = (x**2 + y**2) ** (1/2)

print('Se o cateto oposto for {} e o adjacente for {}, o comprimento da hipotenusa é aproximadamente {:.2f}'. format(x,y,hip))

a = float(input('Coloque o valor do cateto oposto: '))
b = float(input('Coloque o valor do cateto adjacente: '))
hip2 = math.hypot(a,b)

print('Se o cateto oposto for {} e o adjacente for {}, o comprimento da hipotenusa é aproximadamente {:.2f}'. format(x,y,hip2))

w = float(input('Coloque o valor do cateto oposto: '))
z = float(input('Coloque o valor do cateto adjacente: '))
hip = math.sqrt((w**2)+(z**2))

print('Se o cateto oposto for {} e o adjacente for {}, o comprimento da hipotenusa é aproximadamente {:.2f}'. format(x,y,hip))