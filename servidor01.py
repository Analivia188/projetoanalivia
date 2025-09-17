from flask import *

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('dataniver.html')


@app.route('/saberano', methods=['post'])
def saber_ano():
    idade_user = request.form.get('idade')
    ano = 2025 - int(idade_user)
    return render_template('anoniver.html', ano_user=ano)

@app.route('/saberdatanascimento', methods=['post'])
def saber_data_nascimento():
    datanascimento = request.form.get('data_nascimento')
    mes = int(datanascimento.split('-')[1])
    dia = int(datanascimento.split('-')[2])
    if (mes >= 1 and mes <= 6):
        return 'Voce é médico'

    else:
        return 'Voce não é nada, aceite!'

    return render_template(    )

app.run()