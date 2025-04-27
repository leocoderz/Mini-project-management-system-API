from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsProjectManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Project Manager').exists()

class IsDeveloper(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Developer').exists()

class IsAdminOrPMCanEdit(permissions.BasePermission):
    """
    Only Admins and Project Managers can create, update, delete.
    Developers can only read.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True  # Everyone can view
        return (
            request.user.is_staff or
            request.user.groups.filter(name='Project Manager').exists()
        )
