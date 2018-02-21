from django.db import models

from core.models import BaseModel


class Notification(BaseModel):

    message = models.CharField('Mensagem', max_length=255)
    model_name = models.CharField('Nome do Modelo', max_length=100)
    model_id = models.IntegerField('ID do Modelo')

    class Meta:
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
        ordering = ['-created']
