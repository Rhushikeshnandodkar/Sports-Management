from rest_framework.permissions import BasePermission
from .models import *
class IsAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    

            