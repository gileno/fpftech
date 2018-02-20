from django.db import models


class Categoria(models.Model):

    titulo = models.CharField('Título', max_length=100)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'categorias'


class Noticia(models.Model):

    titulo = models.CharField('Título', max_length=100)
    categoria = models.ForeignKey(
        Categoria, models.SET_NULL, verbose_name='Categoria', null=True
    )
    usuario = models.ForeignKey(
        'auth.User', models.SET_NULL, verbose_name='Usuário', null=True
    )
    publicacao = models.DateField('Publicação', null=True, blank=True)
    conteudo = models.TextField('Conteúdo')
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'noticias'
