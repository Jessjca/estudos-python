def separar_digitos(numero):
    numero_str = str(numero)
    for digito in numero_str:
        print(digito)
        
numero = int(input('Digite um numero: '))

if 0 <= numero <= 9999:
    print(separar_digitos(numero))
    
else:
    print('Numero invalido')