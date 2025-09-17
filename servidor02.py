from flask import *

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template('correioelegante.html')

@app.route('/registrar', methods=['POST'])
def registrat_valor():
    nome = request.form.get('pagante')
    valor = request.form.get('valor')

    arquivo = open('registro.txt', 'a')
    linha = f'{nome} - {valor} \n'
    arquivo.write(linha)
    arquivo.close()

app.run()