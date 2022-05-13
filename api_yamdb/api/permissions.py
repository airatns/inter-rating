from rest_framework import permissions


class AdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated
                    and request.user.role == 'admin'))

    # def has_object_permission(self, request, view, obj):
    #     return (request.method in permissions.SAFE_METHODS
    #             or obj.author == request.user)


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
