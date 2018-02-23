from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from .serializers import UserSerializer
from .permissions import IsAdminOrSelf
from .models import User


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve':
            permission_classes = [IsAdminOrSelf]
        elif self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsAuthenticated, IsAdminOrSelf]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAdminOrSelf]
        return [permission() for permission in permission_classes]
