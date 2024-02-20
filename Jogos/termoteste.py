def jogar():
    print('* Bem-vindo ao Termo! *\n')
    acertou, perdeu, tentativas = False, False, 5
    termo = sortear_palavra()
    letras = ['_' for c in range(len(termo))]

    print('----------------------------')
    print(termo)

    while not acertou or not perdeu:
        letras_certas = str(letras).replace("'", '').replace(',', '').removeprefix('[').removesuffix(']')
        print(letras_certas)
        print(f'Chute uma palavra de {len(termo)} letras')
        chute = input('Digite a palavra: ')
        chute = chute.lower()
        while len(chute) != len(termo):
            print('*************************************************')
            print(f'A palavra tem que possuir exatamente {len(termo)} letras!')
            print('*************************************************')
            chute = input('Digite a palavra: ')
        if chute == termo:
            acertou = True
            break
        else:
            verifica_acerto(chute, termo, letras)
            verifica_cor(chute, termo)
            tentativas -= 1
            if tentativas == 1:
                print(f'Você tem {tentativas} tentativa')
            if tentativas == 0:
                perdeu = True
                break
            else:
                print(f'Você tem {tentativas} tentativas')

    verifica_vitoria(acertou, termo)


# ----------------------------------------------------------------
def sortear_palavra():
    import random
    with open('TXT/frutas- termo.txt', 'r') as arquivo:
        palavras = []
        for p in arquivo:
            if p.endswith('\n'):
                p = p[:-1]
            palavras.append(p)
        aleatorio = random.sample(palavras, 1)
        termo = ''
        for c in aleatorio:
            termo += c
        return termo


def verifica_vitoria(acertou, termo):
    if acertou:
        print('\nVocê ganhou')
    else:
        print(f'\nVocê perdeu, a palavra era {termo}')


def verifica_acerto(chute, termo, letras):
    index_chute = -1
    for c in chute:
        index_chute += 1
        index_termo = 0
        for k in termo:
            if c == k and index_chute == index_termo:
                letras[index_chute] = c
            index_termo += 1


def verifica_cor(chute, palavra):
    import colorama
    chute_colorido = ""
    acerto, erro, letra_certa, reset = (colorama.Fore.GREEN, colorama.Fore.BLACK, colorama.Fore.YELLOW,
                                        colorama.Style.RESET_ALL)

    for c in chute:
        contador = 0
        if c not in palavra:
            chute_colorido += (erro + c)
        else:
            chute_colorido += (acerto + c)
    print(chute_colorido + reset)


if __name__ == '__main__':
    jogar()
