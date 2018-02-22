from django.contrib.auth.backends import ModelBackend

from .models import User


class EmailModelBackend(ModelBackend):


    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            user = None
        if user and not user.check_password(password):
            user = None
        return user
