import math # Para importar tudo dessa biblioteca
# ou from math import sqrt, floor para importar apenas  alguns módulos
import emoji

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz quadrada de {num} é {raiz:.2f} {emoji.emojize(":smile:", language="alias") }')

# .ceil - Arredonda pra cima
# .floor - Arredonda pra baixo
# .trunc - Para truncar o valor, remover decimais

