#Binário para octal
def octal(n):
    invertido = str(n)[::-1]
    resultado = ''
    numeros = '000 001 010 011 100 101 110 111'.split()
    for c in range(len(invertido)):
        for k in numeros:
            print(str(invertido[c:c+4]))
            if str(invertido[c:c+4]) == k:
                resultado += k
    return resultado[::-1]

#Binário para decimal
def decimal(n):
    tamanho = len(str(n))-1
    resultado = 0
    for c in str(n):
        if c == '1':
            resultado += (2**tamanho)
        tamanho -= 1
    return resultado

#Binário para hexadecimal
def hexa(n):
    return
