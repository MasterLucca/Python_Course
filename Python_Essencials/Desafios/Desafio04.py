# Leia um valor qualquer e mostre na saida os testes de tipo.
print('Desafio 04\n')

print('Vamos fazer alguns testes!\n')

valor = input('Digite alguma coisa: ')

print('Testes\n')

print(f'É Numérico?: {valor.isnumeric()}\n'
      f'É Decimal?: {valor.isdecimal()}\n'
      f'É String?: {valor.isalnum()}\n'
      f'Está tudo maiúsculo?: {valor.isupper()}'
      )
