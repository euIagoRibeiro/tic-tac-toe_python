
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

exibir_jogo()
