from flask import Flask

app = Flask(__name__)

@app.route('/')
def testePáginaInicial():
  return """<h1>Bem vindo ao site dos</h1>
          <marquee>ESTELIONATÁRIOS</marquee>
          <h1>do BRASIL</h1>"""

@app.route('/usuario/<nome>')
def PagUsuario(nome):
  return f"Olá, {nome} estelionatário(a)"
