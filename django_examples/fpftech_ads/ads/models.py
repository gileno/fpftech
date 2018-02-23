import random

from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy

from templated_email import send_templated_mail

from accounts.models import User


class Ad(models.Model):

    OFFER_TYPE_CHOICES = (
        ('rent', 'Alugar'),
        ('buy', 'Comprar'),
    )

    title = models.CharField('Título', max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.CASCADE, related_name='ads'
    )
    category = models.ForeignKey(
        'Category', models.SET_NULL, blank=False, null=True,
        verbose_name='Categoria',
    )
    description = models.TextField('Descrição')
    offer_type = models.CharField(
        'Tipo da Oferta', max_length=10, choices=OFFER_TYPE_CHOICES
    )
    rank = models.IntegerField('Rank', default=0)
    created = models.DateTimeField('Criada em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def interest(self, email):
        send_templated_mail(
            template_name='interest',
            from_email=email,
            recipient_list=[self.user.email],
            context={
                'ad': self,
                'email': email,
            },
        )
    
    class Meta:
        ordering = ['rank']


class Category(models.Model):

    title = models.CharField('Título', max_length=100)
    created = models.DateTimeField('Criada em', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['title']


def update_ad_rank():
    for ad in Ad.objects.all():
        ad.rank = random.randint(1, 100)
        ad.save()
