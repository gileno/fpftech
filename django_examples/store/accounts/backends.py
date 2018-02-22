from django.contrib.auth.backends import ModelBackend

from rest_framework.authtoken.models import Token

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


class TokenModelBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        auth_header = request.META.get('Authorization', None)
        user = None
        if auth_header:
            auth_header = auth_header.split()
            try:
                token = Token.objects.get(key=auth_header[1])
                user = token.user
            except Token.DoesNotExist:
                pass
        return user
