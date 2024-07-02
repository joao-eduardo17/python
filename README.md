# Projeto em Flask (Udemy-Midiasim)
Um pequeno projeto em Flask para relembrar sua utilização

<br>

## Instalação do Flask
Para a instalação do `Flask`, utilize o comando a seguir no terminal:
```
pip install Flask
```

## Variáveis de ambiente
Para utilizar o `Flask` em um ambiente de desenvolvimento será necessário declarar variáveis de ambiente, então na pasta do projeto flask, crie um arquivo chamado `.flaskenv` e declare as seguintes variáveis:
```
FLASK_APP = app.py
FLASK_DEBUG=true
```
A variável `FLASK_APP` é o nome do seu arquivo python que irá possuir todas as rotas, o padrão geralmente usado é o `app.py`.

Já o `FLASK_DEBUG` serve para que qualquer atualização que o site possuir, não seja necessário rodar o projeto novamente, sendo necessário apenas recarregar a página.

Após isso, utilize o comando a seguir no terminal para as variáveis de ambiente funcionarem:
```
pip install python-dotenv
```

## Criando o ambiente do Flask
No mesmo diretório onde está o arquivo `.flaskenv`, crie um arquivo python (o nome padrão do arquivo é `app.py`, porém qualquer nome pode ser colocado e, se o nome for diferente, deverá ser mudado no arquivo `.flaskenv`), que deverá conter o seguinte código inicialmente:
~~~python
# Importa o flask para sua utilização no arquivo python
from flask import Flask

# Define a variável com a utilização do flask
app = Flask(__name__)

@app.route('/') # Define uma rota padrão para a URL
def principal(): # Cria uma função para retornar algo na URL
  return "Hello World!"
~~~

## Rodando o projeto
Para executar o projeto, utilize o comando a seguir no terminal:
```
flask run
```
A URL padrão do flask é `http://127.0.0.1:5000`

<hr>

# Funções importantes do Flask
O flask possui algumas funções importantes para serem utilizadas tais quais são necessárias para renderizar páginas html e utilizar funções no banco de dados.

## render_template
Uma função muito utilizada é o `render_template`, que é utilizado para renderizar páginas html.

A página html deve estar em uma pasta chamada `templates` para ser renderizada pelo flask.
~~~python
# Importa o render_template junto ao flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
  return render_template("index.html") # No retorno, deve ser posto o nome do arquivo html
~~~


## Utilizar variáveis do Python no HTML
Uma variável do Python pode ser inserida dentro da função que retorna a página html:
~~~python
# RESTO DO CÓDIGO #
@app.route('/')
def principal():
  n1 = 1
  n2 = 2
  return render_template("index.html", n1=n1, n2=n2) # Inserindo as variáveis no html
~~~
E no html, essas variáveis podem ser chamadas por meio de `{{variavel}}`.
~~~html
<body>
  1+2 = {{n1+n2}}
</body>
~~~

## Loops com for utilizando Jinja
Existe como utilizar loops no html utilizando o Jinja. Inserindo uma lista por exemplo, pode-se percorre-la utilizando o `for`.
~~~python
# RESTO DO CÓDIGO #
@app.route('/')
def principal():
  lista = [1,2,3]
  return render_template("index.html", lista=lista)
~~~
Para usar um laço de repetição, utilize o `{% for algo em algumaCoisa %}` e ao fim, colocar `{% endfor %}`.
~~~html
<body>
    {% for numeros in lista %}
        <li>{{numeros}}</li>
    {% endfor %}
</body>
~~~
Para usar dicionários é quase a mesma coisa, apenas mudar de lista para dicionário e no html usar a seguinte sintaxe:
~~~html
<body>
    {% for chave, valor in dicionario.items() %}
        <li>{{chave}} - {{valor}}</li>
    {% endfor %}
</body>
~~~

## Módulo request
O módulo request é um módulo que permite requisições do servidor através dos métodos `GET` e `POST`. O método `POST` manda os dados para o servidor, já o `GET` o requisita.
~~~python
# Importa o request junto ao flask e o render_template
from flask import Flask, render_template, request

# RESTO DO CÓDIGO #
frutas = []

@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST": # Se o método de requisição for o método POST
        if request.form.get("fruta"): # Se a requisição do formulário html não estiver vazia (fruta é o name do input no html)
            frutas.append(request.form.get("fruta")) # Adiciona a fruta na lista de frutas
    return render_template("index.html", frutas=frutas)

# RESTO DO CÓDIGO #
~~~

Agora no html, o `input` deve estar dentro de um `form` com um `action=`, em que seu valor deve estar entre aspas e duas chaves, que dentro deve ter escrito a função `url_for()` para o html saber para onde o método será mandado, no caso é função `principal`, que deve estar entre aspas. Após isso, ainda na tag `form`, deve-se colocar o parâmetro `method=` que deverá ser preenchida com o `"POST"`.

No input deve-se definir o nome para ser utilizado pelo Flask para referenciar a tag.
~~~html
<body>
    <form action="{{url_for('principal')}}" method="POST">
        <input type="text" name="fruta" placeholder="fruta">
        <button>Adicionar</button>
    </form>
</body>
~~~
