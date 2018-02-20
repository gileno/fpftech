from django.shortcuts import render
from django.http import HttpResponse

from .models import Noticia


def inicio(request):
    contexto = {
        'titulo': 'Notícias',
        'noticias': Noticia.objects.all()
    }
    return render(request, 'inicio.html', contexto)
