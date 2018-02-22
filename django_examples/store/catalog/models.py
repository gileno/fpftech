from django.db import models

from notifications.models import Notification

from core.models import BaseModel


class Category(BaseModel):

    name = models.CharField('Nome', max_length=100)
    active = models.BooleanField('Ativo', default=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class ProductQuerySet(models.QuerySet):

    def active(self):
        return self.filter(active=True)
    
    def search(self, q):
        return self.filter(name__icontains=q)


class Product(BaseModel):

    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    quantity = models.PositiveIntegerField('Quantidade', default=0)
    active = models.BooleanField('Ativo', default=True, blank=True)
    categories = models.ManyToManyField(
        Category, related_name='products', blank=True
    )

    objects = ProductQuerySet.as_manager()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'categories': [c.id for c in self.categories.all()],
            'quantity': self.quantity,
        }

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
