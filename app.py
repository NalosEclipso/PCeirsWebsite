from flask import Flask, request, redirect, url_for
import threading
import time

app = Flask(__name__)

emojis = ['🍆', '🤰', '🥱', '💀']
lista_banidos = ['Bernardo', 'niggers', 'Mr. Polar', 'Polar', 'Polar2', 'Niggers', 'Sr. Niggers', 'Sniggers']
lista_membros = ['Guilherme', 'Miguel 🍭', 'Enzo XD', 'Gabriel 🍆']

nome = ''
tempo = 0

def Adicionar_membro(nome):
    n = 0
    while n<10:
        time.sleep(1)
        tempo = n
        print(tempo)
        n+=1
    lista_membros.append(f'(novo) {nome}')

@app.route('/', methods = ['GET', 'POST'])
def cu():
    if request.method == "POST":
        nome = request.form.get('nome')
        print(nome)
        return redirect(f"/{nome}")
    return f"""
            <h1>Olá, pequeno gafanhoto</h1>
            <h2>Digite na caixa abaixo seu nome e te colocaremos na lista de contratação para a maior biqueira do Brasil!😝</h2>
                <form method="POST">
                    <input type="text" name="nome">
                    <button type="submit">Enviar</button>
                </form>
            <h1>Conheça os nossos profissionais já na área:<h1>
            <h1>{", ".join(lista_membros)}</h1>
            <h1>E também os BANIDOS:</h1>
            <h1>{", ".join(lista_banidos)}</h1>
            """

@app.route('/<nome>')
def cu2(nome):
    threading.Thread(target=Adicionar_membro, args=(nome,) ).start()
    return f'''
            Você está na lista de espera, senhor {nome}
            '''
