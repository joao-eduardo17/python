def cifra_de_cesar():
    print("* Bem-vindo ao conversor de Cifra de César! *")
    palavra = input("Escreva aqui a palavra que deseja converter: ")
    senha = int(input("Escolha o número da sua senha: "))
    while senha > 25:
        senha -= 25
    print(senha)
    palavra_secreta = criptografa(palavra, senha)
    print(f"A sua palavra secreta é {palavra_secreta}")


def criptografa(p, s):
    letras = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    for index in range(len(p)):
        senha = s
        for c in letras:
            if p[index] == c:
                while index + senha > 25:
                    resto = senha % 25
                palavra_secreta += ''




if __name__ == '__main__':
    cifra_de_cesar()