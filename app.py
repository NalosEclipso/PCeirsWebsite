from flask import Flask

app = Flask(__name__)

@app.route('/')
def testePáginaInicial():
  return "<h1>FEZES</h1>"
