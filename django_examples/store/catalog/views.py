import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import View
from django.views.decorators import csrf

from .models import Product, Category
from .serializers import ProductModelSerializer


@csrf.csrf_exempt
def products(request, product_id=None):
    status = 200
    if request.method == 'POST':
        product_data = request.POST.copy()
        product = Product(
            name=product_data['name'], description=product_data['description'],
            quantity=int(product_data['quantity'])
        )
        product.save()
        data = json.dumps(product.serialize)
        status = 201
    else:
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            data = json.dumps(product.serialize)
        else:
            data = json.dumps([p.serialize for p in Product.objects.all()])
    return HttpResponse(
        data, content_type='application/json', status=status
    )
#products = csrf.csrf_exempt(products)


class ProductAPI(View):

    def get(self, request, product_id=None):
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            serializer = ProductModelSerializer(product)
            data = json.dumps(serializer.data)
        else:
            serializer = ProductModelSerializer(Product.objects.all(), many=True)
            data = json.dumps(serializer.data)
        return HttpResponse(data, content_type='application/json')

    def post(self, request):
        if request.user.is_authenticated:
            product_data = request.POST.copy()
            product = Product(
                name=product_data['name'], description=product_data['description'],
                quantity=int(product_data['quantity'])
            )
            product.save()
            data = json.dumps(product.serialize)
            status = 201
            return HttpResponse(
                data, content_type='application/json', status=status
            )
        return HttpResponseForbidden()


products = csrf.csrf_exempt(ProductAPI.as_view())
