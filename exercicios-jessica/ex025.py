nome = input('Digite seu nome: ').strip()
print('Seu nome tem Silva, {}?'.format(nome))

if 'silva' in nome.lower():
    print('Sim! Você tem Silva no nome')
else:
    print('Não! Você não tem Silva no nome')