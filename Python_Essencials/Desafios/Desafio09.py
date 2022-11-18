# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print('Vamos ver a tabuada :)\n')

n = int(input('Digite um número para montarmos a tabuada: '))

print('=' * 11)
for i in range(1,11):

    print(f"{n} X {i:2}: {n * i} ")

print('=' * 11)