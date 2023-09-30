def loop_com_break():
    x = 10
    while True:
        print(x)
        if x == 0:
            break
        x -= 1

if __name__ == "__main__":
    loop_com_break()