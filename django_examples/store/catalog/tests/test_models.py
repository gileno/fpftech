from django.test import TestCase

from model_mommy import mommy

from catalog.models import Product, Category


class ProductTestCase(TestCase):

    def setUp(self):
        mommy.make(Product, active=True,  _quantity=10)
        mommy.make(Product, active=False,  _quantity=5)

    def tearDown(self):
        Product.objects.all().delete()
    
    def test_products_active(self):
        self.assertEquals(Product.objects.active().count(), 10)
