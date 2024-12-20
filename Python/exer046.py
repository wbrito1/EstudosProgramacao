import time

c = int(input('Digite os segundos da contagem: '))
for c in range(c, 0, -1):
    print('Faltam {} segundos para o fim do ano'.format(c))
    time.sleep(1)
print('FELIZ ANO NOVO!!')