# Leia alguns valores inseridos em variaveis formate-os para aparecerem em uma frase.
print('Desafio 02\n')

dia = input('Qual é o dia do seu aniversário? ')
mes = input('Qual é o mês do seu aniversário? ')
ano = input('Qual é o ano do seu aniversário? ')

resposta = input(f'O seu aniversário é no dia {dia} de {mes} de {ano} correto? ').upper()

if resposta == 'SIM':
    print('Legal!')
else:
    print('Beleza mano, vaza! ')
