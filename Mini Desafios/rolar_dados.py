def rola_dado():
    import random
    dados = int(input("Escolha o número de dados a ser lançados: "))
    contador, numero_dados, soma_dados = 1, dados, 0
    while numero_dados > 0:
        x = random.randint(1,6)
        if dados == 1:
            print(f"O número do dado é {x}")
            break
        print(f"O {contador}º dado é {x}")
        soma_dados += x
        contador += 1
        numero_dados -= 1
    if dados != 1:
        soma = input("Você deseja a soma dos dados? (Y/N): ").lower()
        match(soma):
            case "y":
                print(f"A soma dos dados é {soma_dados}")
            case "n":
                print("Ok babaca!")

if __name__ == '__main__':
    rola_dado()