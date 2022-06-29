secreto = 'python'
digitadas = []
chances = 3

# laços while chances
while True:
    if chances <= 0:
        print('VOCÊ PERDEU')
        break

    letras = input('Digite uma letra: ')
    if len(letras) > 1:
        print('Apenas uma letra meu querido.')
        continue

    # utilizando metodo append para adicionarmos um unico item
    digitadas.append(letras)

    if letras in secreto:
        print(f'A letra "{letras}" existe na palavra secreta.')
    else:
        print(f'A letra "{letras}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()
     # utilizamos pop para removermos um item que não possui na variavel

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabens você ganhou, a palavra secreta é {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}.')

    if letras not in secreto:
        chances -= 1

    print(f'Você tem {chances} chances.')
    print()



