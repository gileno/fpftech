from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, AdViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'category', CategoryViewSet, base_name='category')
router.register(r'ad', AdViewSet, base_name='ad')
urlpatterns = urlpatterns + router.urls
