
import os

quadro = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

def exibir_jogo():
    print('\n    0   1   2')

    for i, linha in enumerate(quadro):
        print(f'{i} |', end='')
        for elemento in linha:
            print(f' {elemento} |', end='')
        print()
    print()

def selecionar_area():
    while True:

        exibir_jogo()
        jogador_atual = 'X' if turno % 2 == 0 else 'O'
        print(f'Jogador atual: {jogador_atual}')
        linha = int(input('Escolha uma linha: '))
        coluna = int(input('Escolha uma coluna: '))

        if quadro[linha][coluna] == 'X' or quadro[linha][coluna] == 'O':
            os.system('cls')
            print('Este lugar já está ocupado')
        else:
            quadro[linha][coluna] = jogador_atual
            break
    return jogador_atual

turno = 0
for i in range(9):
    
    jogador_atual = selecionar_area()

    def vitoria():
        os.system('cls')
        exibir_jogo()
        print(f'O jogador "{jogador_atual}" venceu o jogo')

    def velha():
        os.system('cls')
        exibir_jogo()
        print('O jogo deu velha')

    if quadro[0][0] == jogador_atual and quadro[0][1] == jogador_atual and quadro[0][2] == jogador_atual:
        vitoria()
        break
    elif quadro[1][0] == jogador_atual and quadro[1][1] == jogador_atual and quadro [1][2] == jogador_atual:
        vitoria()
        break
    elif quadro[2][0] == jogador_atual and quadro[2][1] == jogador_atual and quadro[2][2] == jogador_atual:
        vitoria()
        break
    elif quadro[0][0] == jogador_atual and quadro[1][0] == jogador_atual and quadro[2][0] == jogador_atual:
        vitoria()
        break
    elif quadro[0][1] == jogador_atual and quadro[1][1] == jogador_atual and quadro[2][1] == jogador_atual:
        vitoria()
        break
    elif quadro[0][2] == jogador_atual and quadro[1][2] == jogador_atual and quadro[2][2] == jogador_atual:
        vitoria()
        break
    elif quadro[0][0] == jogador_atual and quadro[1][1] == jogador_atual and quadro[2][2] == jogador_atual:
        vitoria()
        break
    elif quadro[0][2] == jogador_atual and quadro[1][1] == jogador_atual and quadro[2][0] == jogador_atual:
        vitoria()
        break
    else:
        velha()
   
    turno+=1
    os.system('cls')
