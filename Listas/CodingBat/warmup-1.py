def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    return False

#########################################

def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    return False

#########################################

def sum_double(a, b):
    if a == b:
        x = (a+b)*2
        return x
    else:
        x = a+b
        return x

#########################################

def diff21(n):
    if n <= 21:
        x = 21 - n
        return x
    else:
        x = (n - 21)*2
        return x

#########################################

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    return False

#########################################

def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif a+b == 10:
        return True
    else:
        return False

#########################################

def near_hundred(n):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return True
    return False

#########################################

def pos_neg(a, b, negative):
    if a < 0 and b >= 0 and not negative:
        return True
    if a >= 0 and b < 0 and not negative:
        return True
    if a < 0 and b < 0 and negative:
        return True
    return False

#########################################

def not_string(str):
    if 'not' in str[0:3]:
        return str
    return 'not ' + str

#########################################

def missing_char(str, n):
    frente = str[:n]
    tras = str[n+1:]
    return frente + tras

#########################################

def front_back(str):
    if len(str) > 1:
        return str[-1]+ str[1:-1]+ str[0]
    return str

#########################################

def front3(str):
    if len(str) <= 3:
        return str*3
    return str[0:3]*3