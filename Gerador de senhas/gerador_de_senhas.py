def gerador_de_senhas():
    print('* Bem-Vindo ao Gerador de Senhas! *')
    print('Escolha o número de dígitos da sua senha')
    tamanho_senha = int(input('Digite aqui: '))
    senha = ''
    ordem_senha(tamanho_senha)


######################################

def ordem_senha(tamanho_senha):
    import random
    letras = '''a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'''.split()
    numeros = '''0 1 2 3 4 5 6 7 8 9'''.split()
    caracteres = '''! @ # $ % & * _ - = + : ; / ?'''.split()
    tamanho = tamanho_senha
    tamanho_letra, tamanho_numero, tamanho_caracter = 0, 0, 0
    match (1-1): #(random.randint(0,2)):
        case 0:
            while tamanho > 0:
                if tamanho < 1:
                    break
                tamanho_letra += random.randint(1,tamanho)
                tamanho -= tamanho_letra
                if tamanho < 1:
                    break
                tamanho_numero += random.randint(1, tamanho)
                tamanho -= tamanho_numero
                if tamanho < 1:
                    break
                tamanho_caracter += random.randint(1,tamanho)
                tamanho -= tamanho_caracter

        case 1:
            return

        case 2:
            return
    print(tamanho)


if __name__ == '__main__':
    gerador_de_senhas()
