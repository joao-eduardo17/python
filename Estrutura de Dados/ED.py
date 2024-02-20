lista = "joao sandro vitor kalil".split()
# lista[0] -> Retorna joao

lista.sort()  # Ordem alfabética crescente
lista.sort(reverse=True)  # Ordem alfabética decrescente
lista.sort(key=len)  # Ordem de tamanho crescente
lista.sort(key=len, reverse=True)  # Ordem de tamanho decrescente
lista.index("vitor")  # Procura na lista


lista.pop(2) # Remove pelo index
lista.remove("joao") # Remove pelo conteúdo

nomes = ["Diego", "Jhuan", "Kalil"]
notas = [8.75, 9.12, 7.65]

a = {
    "Diego": 8.75,
    "Jhuan": 9.12,
    "Kalil": 7.65
} # Dicionário

import requests
url = ("https://pokeapi.co/api/v2/pokemon/eevee")
dados = requests.get(url).json()

for x in dados['abilities']:
    print(x['ability']['name'])
# Printa as habilidades

