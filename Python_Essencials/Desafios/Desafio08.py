# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

valorMetros = float(input('Digite um valor em métros: '))

valorDecimetro = valorMetros * 10
valorCentimetros = valorMetros * 100
valorMilimetros = valorMetros * 1000

valorDecametro = valorMetros / 10
valorHectometro = valorMetros / 100
valorKilometro= valorMetros / 1000


print(f'\nA conversão de {valorMetros}M para CM é {valorCentimetros}, MM é {valorMilimetros} ')
print(f'\nAgora para KM é {valorKilometro}, HM é {valorHectometro}, DM é {valorDecametro} ')