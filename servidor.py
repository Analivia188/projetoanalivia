#importei o pacote para criar app web
from flask import *

#instanciei o objeto Flask
app = Flask(__name__)

#criando uma rota endpoint
@app.route('/')
def pagina_principal():
    return render_template('quartodia.html')

@app.route('/verificar')
def verificar_convidado():
    nome = request.values.get('nomepessoa')
    convidados = ['Cundy', 'Luiza', 'Natt']


    if nome in convidados:
        return render_template('convidados.html')
    else:
        return 'Infelizmente você não foi convidado'

#executando o servidor
app.run(port=8000)



