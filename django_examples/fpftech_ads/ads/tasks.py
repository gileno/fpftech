from celery import shared_task

from .models import Ad, update_ad_rank


@shared_task
def send_interest(ad_id, email):
    ad = Ad.objects.get(id=ad_id)
    ad.interest(email)


@shared_task
def update_ad_rank_task():
    update_ad_rank()
