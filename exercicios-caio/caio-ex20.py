import random

aluno1 = input('Digite o primeiro aluno: ')
aluno2 = input('Digite o segundo aluno: ')
aluno3 = input('Digite o terceiro aluno: ')
aluno4 = input('Digite o quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
