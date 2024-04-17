velocidade = int(input('Qual a velocidade do veículo? '))
if velocidade > 80:
    print('Você foi multado! Velocidade acima de 80km/h')
    multa = (velocidade - 80)*7
    print('Multa de R${},00'.format(multa))
else:
    print('Dentro do limite de velocidade!')
    
