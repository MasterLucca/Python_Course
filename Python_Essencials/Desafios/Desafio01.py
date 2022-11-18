# Leia um valor inserido, verifique se o usuario possui permissão para participar de um Fã clube
print('Desafio 01\n')

filmeEmComum = 'HOMEM ARANHA'

nome = input('Qual o seu nome? ')
filmePreferido = input('Qual o seu Filme Preferido?' ).upper()

if filmePreferido == filmeEmComum:
    print(f'Bem Vindo, {nome} ao Fã Clube do Homem Aranha!')
else:
    print(f'{nome}, aqui não é o seu Lugar!')