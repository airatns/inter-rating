from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.role == 'admin'
            or request.user.is_superuser == 1
        )
