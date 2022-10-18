peso = float(input('Qual o seu peso? '))
alt = (int(input('Qual a sua altura em centímetros? ')) / 100)

imc = peso / (alt * alt)

print('Seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está obeso.')
elif imc >= 40:
    print('Você está com obesidade mórbida. F')