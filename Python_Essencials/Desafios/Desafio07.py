# Desenvolva um programa que leia duas notas de um aluno e calcule a média das notas.

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

print(f'\nA média da suas notas é: {media:,.2f}')