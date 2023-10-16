def cifra_de_cesar():
    print("* Bem-vindo ao conversor de Cifra de César! *")
    palavra = input("Escreva aqui a palavra que deseja converter: ").lower()
    senha = int(input("Escolha o número da sua senha: "))
    while senha > 25:
        senha -= 25
    palavra_secreta = criptografa(palavra, senha)
    print(f"A sua palavra secreta é {palavra_secreta}")


def criptografa(palavra, senha):
    # global palavra_secreta
    palavra_secreta = ""
    letras = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    index = []
    for c in range(len(palavra)):
        contador = 0
        for k in letras:
            if palavra[c] == " ":
                palavra_secreta += " "
                break
            if palavra[c] == k:
                soma = contador + senha
                if soma >= 26:
                    soma -= 26
                palavra_secreta += letras[soma]
                break
            contador += 1
    return palavra_secreta


if __name__ == '__main__':
    cifra_de_cesar()
