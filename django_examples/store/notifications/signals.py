from django.db import models


notification_created = models.signals.Signal(
    providing_args=['notification', 'level']
)
