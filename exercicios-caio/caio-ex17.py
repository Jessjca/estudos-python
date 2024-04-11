import math

co = float(input('Digite o cateto oposto do triângulo retângulo: '))
ca = float(input('Digite o cateto adjacente do triângulo retângulo: '))
hip = math.hypot(co, ca)
print('O resultado da hipotenusa é: {:.2f}'.format(hip))