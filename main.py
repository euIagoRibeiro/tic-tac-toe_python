
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
    jogador_atual = 'X' if turno % 2 == 0 else 'O'
    linha = int(input('Escolha uma linha: '))
    coluna = int(input('Escolha uma coluna: '))
    quadro[linha][coluna] = jogador_atual

turno = 0
for i in range(9):
    exibir_jogo()
    selecionar_area()
    turno+=1
    os.system('cls')
