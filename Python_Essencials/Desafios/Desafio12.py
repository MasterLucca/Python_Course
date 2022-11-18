# Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Vamos calcular o preço com desconto :)\n')

precoProduto = float(input('Digite o preço do produto: '))

desconto = precoProduto * 5/100

precoProdutoDesconto = precoProduto - desconto

print(f'O Preço do produto com desconto é:{precoProdutoDesconto:.2f} ')