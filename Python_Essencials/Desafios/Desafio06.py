import math

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
print('Desafio 06\n')

n = float(input('Digite um número: '))

print(f' Dobro: {n * 2}\n Triplo: {n * 3:,.2f} \n Raiz quadrada: %.2f' % math.sqrt(n) )