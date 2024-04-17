distancia = int(input('Qual a distância da viagem? '))
if distancia <= 200:
    preco = distancia*0.5
    print('O preço da passagem é de {}'.format(preco))
else:
    preco = distancia*0.45
    print('O preço da passagem é de {}'.format(preco))