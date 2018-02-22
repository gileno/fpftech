from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views
from . import api_views


urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.products, name='product'),
    path(
        'api/products/', api_views.ProductAPIView.as_view(),
        name='products_api'
    ),
    path(
        'api/products/<int:id>/',
        api_views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='products_api'
    ),
]


router = DefaultRouter()
router.register('api2/products', api_views.ProductViewSet, base_name='product')
urlpatterns = urlpatterns + router.urls
