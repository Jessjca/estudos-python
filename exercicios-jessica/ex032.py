ano = int(input('Digite o ano: '))
if ano % 4 == 0:
    if ano % 100 != 0:
        print('O ano {} é um ano bissexto!'.format(ano))
else:
    print('O ano {} não é um ano bissexto.')