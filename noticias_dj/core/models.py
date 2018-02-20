from django.db import models


class Noticia(models.Model):

    titulo = models.CharField('Título', max_length=100)
    publicacao = models.DateField('Publicação', null=True, blank=True)
    conteudo = models.TextField('Conteúdo')
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    modificado_em = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        db_table = 'noticias'
