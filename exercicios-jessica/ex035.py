seg1 = int(input('Digite o primeiro segmento: '))
seg2 = int(input('Digite o segundo segmento: '))
seg3 = int(input('Digite o terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg3 + seg1 and seg3 < seg1 + seg2:
    print('Esses segmentos podem formar um triangulo!')
else:
    print('Com esses segmentos, você não pode formar um triangulo')