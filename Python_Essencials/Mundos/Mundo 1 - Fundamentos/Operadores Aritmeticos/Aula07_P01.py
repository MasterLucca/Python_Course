
nome = input('Olá qual é o seu nome?:')

print('Olá {:=^12}'.format(nome))

# ou

print(f'Olá {nome:=^12}')