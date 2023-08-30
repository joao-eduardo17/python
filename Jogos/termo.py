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
            verifica_cor()
            tentativas -= 1
            if tentativas == 1:
                print(f'Você tem {tentativas} tentativa')
            if tentativas == 0:
                perdeu = True
                break
            else:
                print(f'Você tem {tentativas} tentativas')

            
    verifica_vitoria(acertou, termo)
        
#----------------------------------------------------------------
def sortear_palavra():
    import random
    with open('TXT/frutas- termo.txt', 'r') as arquivo:
        palavras = []
        for p in arquivo:
            if p.endswith('\n'):
                p = p[:-1]
            palavras.append(p)
        aleatorio = random.sample(palavras,1)
        termo = ''
        for c in aleatorio: termo += c
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


def verifica_cor():
    import colorama
    acerto, erro, letra_certa = (colorama.Fore.GREEN), (colorama.Fore.BLACK), (colorama.Fore.YELLOW)
    print(acerto + 'opaopaopa' + erro + 'oas' + letra_certa + 'dhsk')
    print(colorama.Style.RESET_ALL)



if __name__ == '__main__':
    jogar()
    #verifica_cor()
