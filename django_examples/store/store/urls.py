from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('admin/', admin.site.urls),
]
