def jogar_rpg():
    print("Bem-vindo ao RPG mágico :)")
    print("Escolha sua classe:")
    print("1- Arqueiro \n2- Guerreiro \n3- Ladino")
    escolha = int(input())
    personagem = cria_classe(escolha)
    print(f"Sua classe possui os atributos de {personagem}")


def cria_classe(escolha):
    class Classe:
        def __init__(self, vida, forca, agilidade):
            self.vida = vida
            self.forca = forca
            self.agilidade = agilidade

        def __str__(self):
            return f"Vida: {self.vida} - Força: {self.forca} - Agilidade: {self.agilidade}"

    match escolha:
        case 1:
            personagem = Classe(10, 2, 4)
        case 2:
            personagem = Classe(15, 5, 2)
        case 3:
            personagem = Classe(10, 2, 6)
    return personagem


if __name__ == '__main__':
    jogar_rpg()
