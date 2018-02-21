from django.db import models

from notifications.signals import notification_created

from .mail import send_mail_notification


class BaseModel(models.Model):

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        abstract = True


notification_created.connect(send_mail_notification)
