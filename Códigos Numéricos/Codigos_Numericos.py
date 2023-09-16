import binario
import decimal
import octal
import hexadecimal

def introducao():
    print('Bem-vindo ao conversor numérico!')
    print('1 - Binário')
    print('2 - Octal')
    print('3 - Decimal')
    print('4 - Hexadecimal')
    tipo_conversão = int(input('Selecione o tipo do número que deseja converter: '))
    match(tipo_conversão):
        case 1:
            print('\n1 - Octal')
            print('2 - Decimal')
            print('3 - Hexadecimal')
            tipo_convertido = int(input('Para qual tipo você deseja converter? '))
            match(tipo_convertido):
                case 1:
                    print('')


if __name__ == '__main__':
    introducao()