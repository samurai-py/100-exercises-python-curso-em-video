import math
delt = int(input('Digite um ângulo: '))
delta = math.radians(delt)
sen = math.sin(delta)
cos = math.cos(delta)
tan = math.tan(delta)
print('Os seno, cosseno e tangente do ângulo {}° são, respectivamente: {:.4f}, {:.4f} e {:.4f} '.format(delt,sen,cos,tan))