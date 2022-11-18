n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número:'))

soma = n1+n2
divisao = n1 / n2
multiplicacao = n1 * n2
restoDivisao = n1 % n2
divisaoInteira = n1 // n2
potencia = n1**n2

print('Cálculos\n')

print(' Soma: {}\n'.format(soma),
      'Divisão: {}\n'.format(divisao),
      'Divisão Inteira: {}\n'.format(divisaoInteira),
      'Resto de Divisão: {}\n'.format(restoDivisao),
      'Multiplicação: {}\n'.format(multiplicacao),
      'Pôtencia: {}\n'.format(potencia))

# pode usar end = '' para nao quebrar a linha em 2 prints diferentes