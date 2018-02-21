from django.apps import AppConfig
from django.conf import settings


class CatalogConfig(AppConfig):
    
    name = 'catalog'
    verbose_name = 'Catálogo'

    def ready(self):
        if settings.DEBUG:
            print("DEBUG")
        print("inicializando...")
