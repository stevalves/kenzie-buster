from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsEmployeeOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_superuser


class IsYourselfOrSuperuser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj == request.user
