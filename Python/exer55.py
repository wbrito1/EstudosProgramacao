maior_peso = 0
menor_peso = float('inf')

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}º pessoa: '))
    
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
        
print(f'O maior peso é {maior_peso} kg.')
print(f'O menor peso é {menor_peso} kg.')
   
    