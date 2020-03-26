from rest_framework.permissions import BasePermission

SAFE_METHODS_PROFILE = ['GET']


class IsAuthenticatedProfile(BasePermission):
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS_PROFILE or request.user and request.user.is_authenticated):
            return True
        else:
            return False