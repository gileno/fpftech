from django.contrib import admin

from .models import Categoria, Noticia


class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'criado_em', 'modificado_em']
    search_fields = ['titulo']
    list_filter = ['criado_em', 'modificado_em']


class NoticiaAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'categoria', 'publicacao', 'usuario']
    search_fields = ['titulo', 'categoria__titulo']
    list_filter = ['publicacao', 'criado_em', 'modificado_em']
    fields = ['titulo', 'categoria', 'publicacao', 'conteudo']

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
