#Lista I

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
###################################################################
#Lista 2

def triangulo(a,b,c):
    if a>b+c or b>a+c or c>a+b: return 'Não é um triângulo'
    if a==b==c: return 'Equilátero'
    if a==b or a==c or b==c: return 'Isóceles'
    else: return 'Escaleno'

def bissexto(x):
    if x%4==0 and x%100!=0 or x%400==0: return 'Bissexto'
    return 'Não é bissexto'

def 
