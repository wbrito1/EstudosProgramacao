while True:
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Dados inválido! Digite novamente.')
    else:
        break
print(f'Sexo {sexo} registrado com sucesso!')