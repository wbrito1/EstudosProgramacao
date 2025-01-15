from math import factorial

fatorial = 0

while True:
    numero = str(input('Digite um número ou "Q" para sair: ')).upper()
    if numero != 'Q' :
        fatorial = factorial(int(numero))
        print(f'{numero}! = {fatorial}')
    else:
        print('Saindo do programa...')
        break
