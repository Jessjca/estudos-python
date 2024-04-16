cidade = input('Digite a cidade: ').lower().strip()

if (cidade.find('santo')) in [0]:
        print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')