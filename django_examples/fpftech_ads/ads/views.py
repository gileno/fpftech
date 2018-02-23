from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.permissions import IsAdminOrReadOnly, IsAdminOrSelf

from .models import Category, Ad
from .serializers import CategorySerializer, AdSerializer


class CategoryViewSet(ModelViewSet):

    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdViewSet(ModelViewSet):

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    
    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminOrSelf]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
