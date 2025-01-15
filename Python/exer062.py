a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
valor_termo  = int(input('Digite quantos termos quer ver: '))
i = 0

while i != valor_termo:
    if valor_termo != 0:
        termo = a1 + i * r
        i += 1
        print(termo)
    else:
        print('Saindo do programa...')
        break
    if i == valor_termo:
        valor_termo = int(input('Deseja ver mais algum termo?: '))
        
# código do ChatGPT

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
valor_termo = int(input('Digite quantos termos quer ver: '))

termos_exibidos = 0  # Contador de termos exibidos

while valor_termo != 0:
    for i in range(termos_exibidos, termos_exibidos + valor_termo):
        termo = a1 + i * r
        print(termo)
    
    termos_exibidos += valor_termo  # Atualizar o número total de termos exibidos
    
    # Perguntar ao usuário se deseja continuar
    valor_termo = int(input('Deseja ver mais quantos termos? (Digite 0 para sair): '))

print('Programa encerrado.')
