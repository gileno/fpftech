from rest_framework.routers import DefaultRouter

from .views import UserViewSet


urlpatterns = []


router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
urlpatterns = urlpatterns + router.urls
