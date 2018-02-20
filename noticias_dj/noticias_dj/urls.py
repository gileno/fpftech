from django.contrib import admin
from django.urls import path

from core.views import inicio, noticia


urlpatterns = [
    path('', inicio, name='inicio'),
    path('noticias/<int:pk>/', noticia, name='noticia'),
    path('admin/', admin.site.urls),
]
