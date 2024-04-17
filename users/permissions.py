
from rest_framework.permissions import BasePermission

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'user'

class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'administrator'

