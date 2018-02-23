from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('ads/', include('ads.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + [
    path(r'api-auth/', include('rest_framework.urls')),
]
