from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrSelf(BasePermission):

    message = "Você não é admin e nem o cara!"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        else:
            return request.user == obj


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or 
            (request.user.is_authenticated and request.user.is_staff)
        )
