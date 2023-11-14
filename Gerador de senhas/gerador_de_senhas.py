def gerador_de_senhas():
    print('* Bem-Vindo ao Gerador de Senhas! *')
    print('Escolha o número de dígitos da sua senha')
    tamanho_senha = int(input('Digite aqui: '))
    senha = ''
    print('Escolha qual o tipo predominante da sua senha')
    print('1 - Letras\n2 - Números\n3 - Caracteres')
    tipo_predominante = int(input('Digite aqui: '))
    lista = ordem_senha(tamanho_senha, tipo_predominante)
    senha = aleatoriza_senha(lista)


######################################


def ordem_senha(tamanho_senha, tipo_predominante):
    letras = '''a b c d e f g h i j k l m n o p q r s t u v w x y z 
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'''.split()
    numeros = '''0 1 2 3 4 5 6 7 8 9'''.split()
    caracteres = '''! @ # $ % & * _ - = + : ; / ?'''.split()
    tamanho_letra, tamanho_numero, tamanho_caracter = 0, 0, 0
    lista = []
    match tipo_predominante:
        case 1:
            if tamanho_senha % 2 == 0:
                tamanho_letra = tamanho_senha // 2
                tamanho_senha //= 2
                if tamanho_senha % 2 == 0:
                    tamanho_numero = tamanho_senha // 2
                    tamanho_caracter = tamanho_senha // 2
                else:
                    tamanho_numero = tamanho_senha // 2
                    tamanho_caracter = tamanho_senha // 2 + 1
            else:
                tamanho_letra = tamanho_senha // 2 + 1
                tamanho_senha //= 2
                if tamanho_senha % 2 == 0:
                    tamanho_numero = tamanho_senha // 2
                    tamanho_caracter = tamanho_senha // 2
                else:
                    tamanho_numero = tamanho_senha // 2 + 1
                    tamanho_caracter = tamanho_senha // 2
        case 2:
            if tamanho_senha % 2 == 0:
                tamanho_numero = tamanho_senha // 2
                tamanho_senha //= 2
                if tamanho_senha % 2 == 0:
                    tamanho_letra = tamanho_senha // 2
                    tamanho_caracter = tamanho_senha // 2
                else:
                    tamanho_letra = tamanho_senha // 2
                    tamanho_caracter = tamanho_senha // 2 + 1
            else:
                tamanho_numero = tamanho_senha // 2 + 1
                tamanho_senha //= 2
                if tamanho_senha % 2 == 0:
                    tamanho_letra = tamanho_senha // 2 + 1
                    tamanho_caracter = tamanho_senha // 2
                else:
                    tamanho_letra = tamanho_senha // 2 + 1
                    tamanho_caracter = tamanho_senha // 2
        case 3:
            if tamanho_senha % 2 == 0:
                tamanho_caracter = tamanho_senha // 2
                tamanho_senha //= 2
                if tamanho_senha % 2 == 0:
                    tamanho_numero = tamanho_senha // 2
                    tamanho_letra = tamanho_senha // 2
                else:
                    tamanho_numero = tamanho_senha // 2
                    tamanho_letra = tamanho_senha // 2 + 1
            else:
                tamanho_caracter = tamanho_senha // 2 + 1
                tamanho_senha //= 2
                if tamanho_senha % 2 == 0:
                    tamanho_numero = tamanho_senha // 2 + 1
                    tamanho_letra = tamanho_senha // 2
                else:
                    tamanho_numero = tamanho_senha
    lista.append(tamanho_letra)
    lista.append(tamanho_numero)
    lista.append(tamanho_caracter)
    return lista


def aleatoriza_senha(lista):
    pass


if __name__ == '__main__':
    gerador_de_senhas()
