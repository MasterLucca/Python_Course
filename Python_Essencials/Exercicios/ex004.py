print('Vamos fazer alguns testes!\n')

valor = input('Digite alguma coisa: ')

print('Testes\n')

print(f'O tipo primitivo desse valor é: {type(valor)}\n'
      f'É Numérico?: {valor.isnumeric()}\n'
      f'É Decimal?: {valor.isdecimal()}\n'
      f'É Alfanúmerico?: {valor.isalnum()}\n'
      f'É Alfabético?: {valor.isalpha()}\n'
      f'Está tudo maiúsculo?: {valor.isupper()}\n'
      f'Está tudo minúsculo?: {valor.islower()}\n'
      f'Está Capitalizada?: {valor.istitle()}')