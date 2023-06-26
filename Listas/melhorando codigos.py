def soma(n1,n2):
    return n1+n2

def metros(m):
    return m*1000

def segundos(d,h,m,s):
    return (d*86400)+(h*3600)+(m*60)+s

def salario(s,a):
    return f'{((a/100)*s)} e {((a/100)*s)+s}'

def desconto(p,d):
    return f'{(d/100)*p} e {p-((d/100)*p)}'

def viagem(d,v):
    return d/v

def celsius(t):
    return 9*t / 5+32

def fahrenheit(f):
    return (f - 32) * 5/9

def carro_alugado(km,d):
    return (km*0.15)+(d*60)

def cigarros(c,a):
    return f'{((a*365)*c)/144:.0f}'

def elevado():
    return len(str(2**100))
