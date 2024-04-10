import math

angulo_graus = int(input('Digite um ângulo: '))
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print('Seno {}, Cosseno {}, Tangente {}'.format(seno, cosseno, tangente))