def adivinhacao():
    from random import randint
    print("Adivinhe o número de 1 a 100")
    numero_secreto = randint(1, 100)
    tentativas, vitoria = 5, False
    while tentativas > 0:
        print(f"Ainda resta {tentativas} tentativas")
        chute = int(input("Digite o seu chute: "))
        if numero_secreto == chute:
            print(f"Parabéns, você venceu em {5 - tentativas + 1} tentativas")
            vitoria = True
            break
        elif numero_secreto > chute:
            print(f"O número é maior que {chute}")
        else:
            print(f"O número é menor que {chute}")
        tentativas -= 1
    if not vitoria:
        print(f"Que pena! O número era {numero_secreto}")
if __name__ == '__main__':
    adivinhacao()