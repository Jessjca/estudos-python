import math #ou também pode ser utilizar: from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

import random
num = random.random(1, 100)
print(num)

import emoji
print(emoji.emojize('Olá bosta :pile_of_poo:', use_alies=True))