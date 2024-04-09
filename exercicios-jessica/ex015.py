km = float(input('Quantos KM foram percorridos?'))
dias = int(input('Por quantos dias o carro foi utilizado?'))
total_dias = dias*60
total_km = km*0.15
total = total_dias + total_km
print('O total a pagar pelo uso do veículo durante {} dias e com {}km rodados é de R${}'.format(dias, km, total))