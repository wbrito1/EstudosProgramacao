from datetime import date
atual = date.today().year
contador = 0
for i in range(7):
    ano = int(input('Digite o ano de nascimento: '))
    if atual - ano >= 21:
        contador += 1
print(f'{contador} de 7 pessoas já atingiram a maioridade')