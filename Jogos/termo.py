def jogar():
    print('* Bem-vindo ao Termo! *\n')
    acertou, perdeu, tentativas = False, False, 5
    termo = sortear_palavra()
    letras = ['_' for c in range(len(termo))]
    print(letras)
    print('----------------------------')
    print(termo)
    
    while not acertou or not perdeu:
        print(f'Chute uma palavra de {len(termo)} letras')
        chute = input('Digite a palavra: ')
        if chute == termo:
            acertou = True
            break
        else:
             tentativas -= 1
             if tentativas == 0:
                print('Você perdeu')
                break
                
    if acertou:
        print('você ganhou')
        
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



if __name__ == '__main__':
    jogar()
