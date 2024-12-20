n1 = int(input('Digite o inicio: '))
n2 = int(input('Digite o fim: '))
s = 0
for c in range(n1, n2):
    if(c % 2 != 0  and c % 3 == 0):
        s += c
print('A soma de todos os numeros entre 1 e 500 é {}'.format(s))
print('FIM')
    