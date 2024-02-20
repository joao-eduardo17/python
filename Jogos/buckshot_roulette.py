import colorama
import random

def intro():
    print("Seja bem-vindo a roleta russa com o diablo")
    print("1- Iniciar")
    print("2- Opções")
    print("3- Multijogador")
    escolha = int(input())
    if escolha == 1:
        #jogar()
        pass
    elif escolha == 2:
        opcoes()
    else:
        multiplayer()


def opcoes(): #fds
    pass


def multiplayer():
    cores, limpa = [0, colorama.Fore.YELLOW, colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.BLUE, colorama.Fore.CYAN,
             colorama.Fore.MAGENTA, colorama.Fore.WHITE], colorama.Style.RESET_ALL

    #Dados do Player 1
    itens_p1 = []
    print("Player 1, digite seu nome e a cor que deseja")
    nome_p1 = input("Nome: ")
    print("1 - Amarelo \n2 - Vermelho \n3 - Verde \n4 - Azul \n5 - Ciano \n6 - Magenta \n7 - Branco")
    cor_p1 = int(input())
    for c in range(8):
        if c == cor_p1:
            cor_p1 = cores[c]
    print(cor_p1 + f"Seu nome é {nome_p1}" + limpa)

    #Dados do Player 2
    itens_p2 = []
    print("Player 2, digite seu nome e a cor que deseja")
    nome_p2 = input("Nome: ")
    print("1 - Amarelo \n2 - Vermelho \n3 - Verde \n4 - Azul \n5 - Ciano \n6 - Magenta \n7 - Branco")
    cor_p2 = int(input())
    for c in range(8):
        if c == cor_p2:
            cor_p2 = cores[c]
    print(cor_p2 + f"Seu nome é {nome_p2}" + limpa)


def itens(rodada, itens_p):
    itens = ["l", "a", "r", "s"]
    k = 0
    match rodada:
        case 2:
            if len(itens_p) == 8:
                return
            while len(itens_p) < 8:
                if k == 2:
                    break
                itens_p.append(random.choice(itens))
                k += 1
        case 3:
            if len(itens_p) == 8:
                return
            while len(itens_p) < 8:
                if k == 4:
                    break
                itens_p.append(random.choice(itens))
            k += 1
    print(itens_p)
    return itens_p


def moeda(escolha):
    faces = [0, 1, 2]
    x = random.randint(1, 2)
    if escolha == faces[x]:
        return 1
    return 0
    # 1 é quem escolheu


balas 1 rodada: 3 cheias 1 vazia










if __name__ == '__main__':
    intro()
