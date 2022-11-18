# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('Bora pegar uns dólar!')

dinheiroDisponivelCarteira = float(input('\nQuanto dinheiro você tem disponivel R$: '))

qtdDolar = dinheiroDisponivelCarteira / 5.46

print(f'Você pode comprar US${qtdDolar:.2f} dólares com R${dinheiroDisponivelCarteira:.2f} Reais')