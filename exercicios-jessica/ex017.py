import math

cat_oposto = int(input('Digite o cateto oposto: '))
cat_adj = int(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(cat_oposto, cat_adj)
print(hipotenusa)