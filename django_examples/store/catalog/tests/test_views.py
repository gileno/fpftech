import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APIClient

from model_mommy import mommy

from catalog.models import Product, Category


class ProductViewTesteCase(TestCase):

    def setUp(self):
        mommy.make(Product, active=True, _quantity=5)
        self.product = Product.objects.first()
        self.category = mommy.make(Category)
        self.product.categories.add(self.category)
        self.client = Client()
    
    def tearDown(self):
        Product.objects.all().delete()
        Category.objects.all().delete()

    def test_list_create_ok(self):
        url_list = reverse('product-list')
        response = self.client.get(url_list)
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEquals(len(data), 5)
        product_data = {
            'name': 'Test product', 'description': 'Ok', 'quantity': 2
        }
        response = self.client.post(url_list, product_data)
        self.assertEqual(Product.objects.count(), 6)
    
    def test_auth(self):
        from accounts.models import User
        from rest_framework.authtoken.models import Token
        user = mommy.make(User)
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url_detail = reverse('products_api', args=[self.product.pk])
        response = client.get(url_detail)
        self.assertEqual(response.status_code, 200)
