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
```
# Importa o flask para sua utilização no arquivo python
from flask import Flask

# Define a variável com a utilização do flask
app = Flask(__name__)
```

## Rodando o projeto
Para executar o projeto, utilize o comando a seguir no terminal:
```
flask run
```
A URL padrão do flask é `http://127.0.0.1:5000`
