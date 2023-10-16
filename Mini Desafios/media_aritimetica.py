def media_aritimetica():
    contador, soma = 0, 0
    print()
    while True:
        numero = input("Digite o número: ")
        if numero == '':
            break
        soma += float(numero)
        contador += 1
    media = soma / contador
    print(f"\nA média é {media}")

def moda():
    return

def mediana():
    lista = []
    while True:
        numero = input("Digite o número: ")
        if numero == '':
            break
        lista.append(numero)
    metade = int(len(lista)/2)
    match(len(lista)%2):
        case 0:
            print(f"As medianas são: {lista[metade-1]} e {lista[metade]}")
        case 1:
            print(f"A mediana é {float(lista[int(metade)])}")

if __name__ == '__main__':
    print("O que você deseja calcular?")
    print("1 - Média \n2 - Moda \n3 - Mediana")
    escolha = int(input("Digite sua escolha: "))
    match escolha:
        case 1:
            media_aritimetica()
        case 2:
            moda()
        case 3:
            mediana()
