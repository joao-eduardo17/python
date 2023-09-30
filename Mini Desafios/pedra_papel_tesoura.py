def ppt():
    import random, colorama
    vitoria, empate, derrota = (colorama.Fore.GREEN), (colorama.Fore.YELLOW), (colorama.Fore.RED)
    jogar = True
    while jogar:
        ppt = "pedra papel tesoura".split()
        print("Escolha entre Pedra, Papel ou Tesoura")
        print("1 - Pedra \n2 - Papel \n3 - Tesoura")
        escolha_jogador = int(input("Digite sua escolha: "))
        print(f"Sua escolha é {ppt[escolha_jogador-1]}")
        print("\nAgora é a vez do computador!")
        escolha_computador = random.randint(1,3)
        print(f"A escolha do computador foi {ppt[escolha_computador-1]}")
        print(f"\nSerá {ppt[escolha_jogador-1]} X {ppt[escolha_computador-1]}")
        if escolha_computador == escolha_jogador:
            print(empate + "Empate!")
            print(colorama.Style.RESET_ALL)
            print("Deseja jogar de novo?")
            jogar_denovo = input("Digite sua escolha (Y/N) ").lower()
            if jogar_denovo == "n":
                jogar = False
                break
            else:
                continue
        elif escolha_computador == 1 and escolha_jogador == 2:
            print(vitoria + "Você venceu!")
            print(colorama.Style.RESET_ALL)
        elif escolha_computador == 1 and escolha_jogador == 3:
            print(derrota + "Você perdeu!")
            print(colorama.Style.RESET_ALL)
        elif escolha_computador == 2 and escolha_jogador == 1:
            print(derrota + "Você perdeu!")
            print(colorama.Style.RESET_ALL)
        elif escolha_computador == 2 and escolha_jogador == 3:
            print(vitoria + "Você venceu!")
            print(colorama.Style.RESET_ALL)
        elif escolha_computador == 3 and escolha_jogador == 1:
            print(vitoria + "Você venceu!")
            print(colorama.Style.RESET_ALL)
        else:
            print(derrota + "Você perdeu!")
            print(colorama.Style.RESET_ALL)
        jogar_denovo = input("\nDeseja jogar novamente?(Y/N) ").lower()
        if jogar_denovo == "n":
            break
    print("Obrigado por jogar!")

if __name__ == '__main__':
    ppt()