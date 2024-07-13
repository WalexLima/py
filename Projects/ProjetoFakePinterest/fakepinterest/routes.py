from flask import render_template
from fakepinterest import app  # Importando a instância do app Flask

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)
