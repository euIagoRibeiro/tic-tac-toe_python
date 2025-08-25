
quadro = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

def exibir_jogo():
    for linha in quadro:
        for elemento in linha:
            print(f'| {elemento} |', end='')
        print()

exibir_jogo()
