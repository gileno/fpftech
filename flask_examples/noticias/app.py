import dataset

from flask import Flask, render_template

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


app.config['DEBUG'] = True
app.run()