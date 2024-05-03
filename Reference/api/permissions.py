from rest_framework.permissions import IsAdminUser

class IsAdmin(IsAdminUser):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff