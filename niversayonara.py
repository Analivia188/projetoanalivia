from flask import *
from flask import Flask

app: Flask = Flask(__name__)
crushs = ['jose']

@app.route('/')
def home_page():
    return render_template('say.html')

@app.route('/administradora')
def mostrar_pag_senha():
    return render_template('saysenha.html')

@app.route('/adicionarpessoas', methods=['post'])
def adicionar_pessoas():
    global crushs
    nome = request.form.get('nome')
    crushs.append(nome)
    mensagem = nome + ' foi adicionado com sucesso'


    return render_template('logado.html', msg = mensagem )

@app.route('/removerpessoas', methods=['post'])
def remover_pessoas():
    global crushs
    nome = request.form.get('nome')
    if nome in crushs:
        crushs.remove(nome)
        mensagem = nome + ' foi removido com sucesso'
    else:
        mensagem = nome + 'não consta na lista'
        return render_template('logado.html')

@app.route('/verificarsenha', methods=['post'])
def verificar_senha():
    senha = request.form.get('senha')
    if senha == '2007':
        return render_template('logado.html')
    else:
        return render_template('say.html')


@app.route('/acharamor', methods=['post'])
def verificar_amado():
    nome_pessoa = request.form.get('candidato')

    if nome_pessoa.lower() in crushs:
        return render_template('elaqueryou.html')

    else:
        return render_template('elanaoqueryou.html')


if __name__ == '__main__':
    app.run()