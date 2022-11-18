# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e o quanto de tinta
# é necessaria para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

print('Vamos calcular a quantidade de tinta :)\n')

larguraParedeMetros = float(input('Digite a largura de sua parede em Métros: '))
alturaParedeMetros = float(input('Digite a largura de sua parede em Métros: '))

area = larguraParedeMetros * alturaParedeMetros
totalTintaNecessaria = area / 2

print( f'A sua parede tem área de {area}m² então Você precisará de {totalTintaNecessaria:.2f} litros de tinta para pintar a sua parede.')