from django.db import models

from notifications.models import Notification

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
    quantity = models.PositiveIntegerField('Quantidade', default=0)
    categories = models.ManyToManyField(
        Category, related_name='products', blank=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


def post_save_product(**kwargs):
    product = kwargs['instance']
    if product.quantity <= 0:
        notification = Notification()
        notification.model_id = product.id
        notification.model_name = str(product.__class__)
        notification.message = 'Produto com quantidade menor que zero'
        notification.save()


models.signals.post_save.connect(post_save_product, sender=Product)
