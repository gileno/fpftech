from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response

from accounts.permissions import IsAdminOrReadOnly, IsAdminOrSelf

from .models import Category, Ad
from .serializers import CategorySerializer, AdSerializer, InterestSerializer
from .tasks import send_interest


class CategoryViewSet(ModelViewSet):

    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdViewSet(ModelViewSet):

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['$title', '$category__title', '$description']
    
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
    
    @detail_route(methods=['POST'], permission_classes=[AllowAny])
    def interest(self, request, pk=None):
        ad = self.get_object()
        serializer = InterestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_interest.delay(ad_id=ad.id, email=serializer.data['email'])
        return Response({'status': 'Interesse enviado com sucesso'}, status=201)
