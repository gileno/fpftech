from django.db import models

from core.models import BaseModel


class Category(BaseModel):

    name = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Product(BaseModel):

    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    categories = models.ManyToManyField(
        Category, related_name='products', blank=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
