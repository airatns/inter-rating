from rest_framework import permissions

ADMIN = 'admin'
MODERATOR = 'moderator'


class IsObjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class IsAdminOrModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role in [ADMIN, MODERATOR]
