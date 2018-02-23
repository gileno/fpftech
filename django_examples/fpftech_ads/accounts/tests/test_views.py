from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.authtoken.models import Token

from model_mommy import mommy

from accounts.models import User
from accounts.views import UserViewSet


class UserViewSetTestCase(TestCase):

    def setUp(self):
        self.user = mommy.prepare(User, username='admin', name='admin')
        self.user.is_staff = True
        self.user.set_password('123')
        self.user.save()
        self.token = Token.objects.create(user=self.user)
    
    def tearDown(self):
        User.objects.all().delete()
        Token.objects.all().delete()
    
    def test_list_user(self):
        client = APIClient()
        url_list = reverse('user-list')
        response = client.get(url_list)
        self.assertEquals(response.status_code, 401)
        client.login(username='admin', password='123')
        response = client.get(url_list)
        self.assertEquals(response.status_code, 200)
    
    def test_update_user(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url_update = reverse('user-detail', kwargs={'pk': self.user.pk})
        data = {'name': 'administration'}
        response = client.patch(url_update, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.get(pk=self.user.pk).name, 'administration')
