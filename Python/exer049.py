while True:
    tabuada = int(input("Digite a tabuada que deseja ver ou 0 para encerrar o programa: "))
    if tabuada == 0:
        print('Fim da tabuada!')
    else:
        contador = 0
        for i in range(11):
            res = tabuada * contador
            print(f'{tabuada} X {contador} = {res}')
            contador += 1