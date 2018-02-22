from django.urls import path

from . import views


urlpatterns = [
    path('obtain-token/', views.obtain_token, name='obtain_token'),
]