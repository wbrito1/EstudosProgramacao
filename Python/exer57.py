while True:
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Dados inválido! Digite novamente.')
    else:
        break
print('FIM')