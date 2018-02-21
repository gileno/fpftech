from django.core.mail import send_mail


def send_mail_notification(**kwargs):
    notification = kwargs['notification']
    send_mail(
        'Notificação criada', notification.message, 'admin@admin.com',
        ['notificacao@admin.com']
    )
