import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators import csrf

from .models import Product, Category


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
