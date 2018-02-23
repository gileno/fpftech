from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'category', CategoryViewSet, base_name='category')
urlpatterns = urlpatterns + router.urls
