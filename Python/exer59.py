valor01 = int(input('Digite um valor: '))
valor02 = int(input('Digite outro valor: '))

soma = valor01 + valor02
mult = valor01 * valor02
maior = valor01 > valor02
novos_numeros = ''
sair = 'S'

menu = 0

while True:
    print('''Menu:
                     [1] Somar
                     [2] Multiplicar
                     [3] Maior
                     [4] Novos números
                     [5] Sair do programa''')
    menu = int(input('Digite qual opção deseja: '))
    
    if menu == 1:
        soma
    print(f'O resultado da operação é {soma}')
    
    if menu == 2:
        mult
    print(f'O resultado da operação é {mult}')
    
    if menu == 3:
        maior
    print(f'O maior número é {maior}')
