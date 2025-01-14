
s = 0
for i in range(1, 501):
    if(i % 2 != 0  and i % 3 == 0):
        s += i
print('A soma de todos os numeros entre 1 e 500 é {}'.format(s))
print('FIM')
    