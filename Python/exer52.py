numero = int(input('Digite um número inteiro: '))

if numero > 1:  # Verifica se o número é maior que 1
    eh_primo = True  # Assume que o número é primo
    for i in range(2, int(numero ** 0.5) + 1):  # Testa divisores até a raiz quadrada
        if numero % i == 0:  # Se o número for divisível por 'i'
            eh_primo = False  # Não é primo
            break  # Interrompe o loop, pois já sabemos que não é primo
    if eh_primo:
        print(f'O número {numero} é um número primo!')
    else:
        print(f'O número {numero} não é um número primo!')
else:
    print(f'O número {numero} não é um número primo!')
