from flask import Flask, render_template

app = Flask('noticias')


@app.route('/')
def index():
    titulo = 'Notícias'
    noticias = [
        'Notícia 1', 'Notícia 2', 'Notícia 3'
    ]
    return render_template(
        'index.html', titulo=titulo, noticias=noticias
    )


app.config['DEBUG'] = True
app.run()