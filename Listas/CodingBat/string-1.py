def hello_name(name):
    return 'Hello ' + name + '!'

#########################################

def make_abba(a, b):
    return a + b + b + a

#########################################

def make_tags(tag, word):
    return '<'+tag+'>'+word+'</'+tag+'>'

#########################################

def make_out_word(out, word):
    metade = len(out)/2
    return out[:metade] + word + out[metade:]

#########################################

def extra_end(str):
    return str[-2:]*3

#########################################

def first_two(str):
    if len(str) >=2:
        return str[:2]
    return str

#########################################

def first_half(str):
    metade = len(str)//2
    return str[:metade]

#########################################

def without_end(str):
    if len(str) >= 2:
        return str[1:-1]
    return str

#########################################

def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    return a + b + a

#########################################

def non_start(a, b):
    if len(a) > 1 and len(b) > 1:
        return a[1:] + b[1:]
    return a[1:] + b[1:]

#########################################

def left2(str):
    if len(str) >= 2:
        return str[2:] + str[:2]