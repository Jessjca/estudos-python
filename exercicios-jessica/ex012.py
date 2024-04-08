preco = int(input('Digite o preço do produto: '))
desconto = preco * 0.05
novo_preco = preco - desconto
print('O produto de {} reias, está com desconto de 5%, seu novo preço é de {}'.format(preco, novo_preco))