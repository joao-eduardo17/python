import requests

# Procurar no json uma descrição específica em um idioma específico
url = 'https://pokeapi.co/api/v2/ability/battle-armor'
dados = requests.get(url).json()
for x in dados['effect_entries']:
    if x['language']['name'] == 'en':
        print(x['short_effect'])
print('\n')

# Deputados

# Procurar no json os dados específicos dos deputados
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
dados = requests.get(url).json()
for x in dados['dados']:
    if x['siglaPartido'] == 'PT' and x['siglaUf'] == 'MA':
        print(x['nome'])
        arq = x['nome'] + '.jpg'
        f = open(arq, 'wb')
        foto = requests.get(x['urlFoto']).content
        #f.write(foto)
        f.close()
print('\n')

# Gastos totais de um deputado
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ordem=ASC&ordenarPor=ano&pagina='
total = 0
for pagina in range(1, 44):
    rq = requests.get(url + str(pagina) + '&itens=15').json()
    for c in rq['dados']:
        total += float(c['valorDocumento'])
print(f'R${total:.2f}')

# Ordenar
