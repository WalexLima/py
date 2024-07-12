## Para iniciar o projeto, vamos usar o Flask. pip install flask
## Próximo passa é importar
from flask import Flask

## 1° Criação do site
app = Flask(__name__)

## 2° Criação de rota: Caminho do link do site.
@app.route("/")

## 3° Criação do site.
def homepage():
    return "FakePinterest - Meu primeiro site no ar"

## 4° Algumas boas práticas para atualizar nosso site.
if __name__ == "__name__":
    app.run(debug=True)