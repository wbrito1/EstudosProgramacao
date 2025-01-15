import random

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tentativas = 0
jogador = 0
maquina = random.choice(lista)
print('A máquina ja escolheu um número!')

while True:
    jogador = int(input('Digite o seu número: '))
    tentativas += 1
    if jogador != maquina:
        print('Você não acertou, tente novamente!')
    if jogador == maquina:
        print(f'Parabéns, Você ganhou! Você precisou de {tentativas} tentativas para acertar.')
    
# Código Guanabara

computador = random.randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')