km = float(input('Quantos kilometros foram rodados? '))
dias = float(input('Quantos dias você usou o carro? '))
kmc = km*0.15
diasc = dias*60
calc = kmc+diasc
print('O valor do aluguel do veículo ficou em R${}.'.format(calc))
