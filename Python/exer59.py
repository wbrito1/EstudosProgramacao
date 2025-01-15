from time import sleep
valor01 = int(input('Digite um valor: '))
valor02 = int(input('Digite outro valor: '))

menu = 0

while menu != '5':
    print('''\nMenu:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    
    menu = str(input('Digite qual opção deseja: '))
   
    
    if menu == '1':
        soma = valor01 + valor02
        print(f'O resultado da operação é {soma}')

    elif menu == '2':
        mult = valor01 * valor02
        print(f'O resultado da operação é {mult}')

    elif menu == '3':
        maior = max(valor01, valor02)
        print(f'O maior número é {maior}')
    
    elif menu == '4':
        valor01 = int(input('Digite um novo valor: '))
        valor02 = int(input('Digite outro novo valor: '))
    
    elif menu == '5':
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente!')
        
# Código do Guanabara

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print(''' 
        [1] Somar
        [2] Multiplcar
        [3] Maior
        [4] Novos Números
        [5] Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} = {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} X {n2} = {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente Novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')