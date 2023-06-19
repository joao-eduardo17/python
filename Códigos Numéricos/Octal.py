def octal(n):
    r = ''
    if n <= 8:
        return n
    while n > 8:
        r = r + str(n%8)
        n = n//8
    x = str(n) + str(r[::-1])
    return int(x)

def decimal():
    return
