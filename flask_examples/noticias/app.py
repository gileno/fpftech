import dataset

from flask import Flask, render_template, jsonify, request

app = Flask('noticias')


def conexao():
    return dataset.connect('sqlite:///noticias.db')


@app.route('/')
def index():
    titulo = 'Notícias'
    tabela_noticias = conexao()['noticias']
    noticias = tabela_noticias.all()
    return render_template(
        'index.html', titulo=titulo, noticias=noticias
    )


@app.route('/noticias/<int:noticia_id>')
def detalhes(noticia_id):
    tabela_noticias = conexao()['noticias']
    noticia = tabela_noticias.find_one(id=noticia_id)
    return render_template('noticia.html', noticia=noticia)


@app.route('/api/noticias/', methods=['GET', 'POST'])
@app.route('/api/noticias/<int:noticia_id>')
def noticias_api(noticia_id=None):
    tabela_noticias = conexao()['noticias']
    if noticia_id is None:
        if request.method == 'POST':
            dados = request.form.copy()
            noticia_id = tabela_noticias.insert(dados)
            noticia = tabela_noticias.find_one(id=noticia_id)
            return jsonify(noticia), 201
        else:
            noticias = tabela_noticias.all()
        return jsonify(results=[n for n in noticias])
    else:
        noticia = tabela_noticias.find_one(id=noticia_id)
        return jsonify(noticia)
    


app.config['DEBUG'] = True
app.run()