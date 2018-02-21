from django.db import models

from core.models import BaseModel

from .signals import notification_created


class Notification(BaseModel):

    message = models.CharField('Mensagem', max_length=255)
    model_name = models.CharField('Nome do Modelo', max_length=100)
    model_id = models.IntegerField('ID do Modelo')

    def save(self, *args, **kwargs):
        result = super(Notification, self).save(*args, **kwargs)
        notification_created.send(
            sender=self, notification=self, level='save_method'
        )
        return result

    class Meta:
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
        ordering = ['-created']
