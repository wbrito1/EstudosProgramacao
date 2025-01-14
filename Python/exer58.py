import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tentativas = 1
jogador = 0
maquina = random.choice(lista)
print('A máquina ja escolheu um número!')

while True:
    jogador = int(input('Digite o seu número: '))
    if jogador != maquina:
        print('Você não acertou, tente novamente!')
    if jogador == maquina:
        print(f'Parabéns, Você ganhou! Você precisou de {tentativas} tentativas para acertar.')
    tentativas += 1


