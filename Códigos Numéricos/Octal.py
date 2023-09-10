#Octal para binário
def binario(n):
    n = str(n)
    resultado = ''
    numeros = '000 001 010 011 100 101 110 111'.split()
    for c in n:
        for contador in range(len(numeros)):
            if c == str(contador):
                resultado += numeros[contador]
                break
    return int(resultado)

#Octal para decimal
def decimal(n):
    resultado = 0
    index = len(str(n)) - 1
    for c in str(n):
        resultado += (int(c)*(8**index))
        index -= 1
    return resultado

#Octal para Hexadecimal
def hexa(n):
    
