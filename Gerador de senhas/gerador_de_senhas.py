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
            tamanho_letra = tamanho//2
            tamanho = tamanho // 2
            tamanho_numero = tamanho // 2
            tamanho = tamanho // 2
            tamanho_caracter = tamanho
            while tamanho_numero + tamanho_caracter + tamanho_letra != tamanho_senha:
                x = random.randint(0,3)

            print(tamanho)
            print(tamanho_letra)
            print(tamanho_caracter)
            print(tamanho_numero)


        case 1:
            return

        case 2:
            return


if __name__ == '__main__':
    gerador_de_senhas()
