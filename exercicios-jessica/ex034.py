salario = float(input('Digite o salário: '))
if salario > 1.250:
    aumento = salario+(salario*0.1)
    print(aumento)
else:
    aumento = salario+(salario*0.15)
    print(aumento)