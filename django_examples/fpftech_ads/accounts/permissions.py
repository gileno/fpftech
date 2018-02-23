from rest_framework.permissions import BasePermission


class IsAdminOrSelf(BasePermission):

    message = "Você não é admin e nem o cara!"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        else:
            return request.user == obj
