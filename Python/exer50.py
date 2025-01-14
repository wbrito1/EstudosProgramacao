lista = []
soma_pares = 0
for _ in range(6):
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    if numero % 2 == 0:
        soma_pares += numero
        
if soma_pares > 0:
    print(f'A soma de todos os números pares é {soma_pares}')
else:
    print(f'Não ha nenhum número par na lista {lista}')