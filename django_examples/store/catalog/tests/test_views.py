import json

from django.test import TestCase, Client
from django.urls import reverse

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
    
    def test_retrieve_update_delete_ok(self):
        url_detail = reverse('product-detail', args=[self.product.pk])
        response = self.client.get(url_detail)
        data = json.loads(response.content)
        self.assertEqual(data['id'], self.product.pk)
        product_data = {
            'name': 'Test product', 'description': 'Ok', 'quantity': 2
        }
        response = self.client.put(url_detail, product_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEquals(data['name'], 'Test product')
