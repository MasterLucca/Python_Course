# Faça um algoritmo que leia um salário de um funcionário e mostre seu novo salário com 15% de aumento.

print('Vamos calcular o aumento do seu salário :)')

salario = float(input('Digite seu sálario R$:'))

desconto = salario * 15/100
salarioReajustado = salario + desconto

print(f'Seu sálario com aumento de 15% é de R${salarioReajustado:.2f} Reais')
