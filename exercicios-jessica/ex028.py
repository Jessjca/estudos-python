import random

lista = [0,1,2,3,4,5]
numero_pensado = random.choice(lista)
chute = int(input('Em qual número de 0 a 5 estou pensando? '))
if chute == numero_pensado:
    print('Parabéns, você acertou! Eu pensei no número {}'.format(numero_pensado))
else:
    print('Você errou! Eu pensei no número {}'.format(numero_pensado))
