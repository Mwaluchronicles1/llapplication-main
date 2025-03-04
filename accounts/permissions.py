from rest_framework import permissions


class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'SUPER_ADMIN'


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['ADMIN', 'SUPER_ADMIN']


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['MODERATOR', 'ADMIN', 'SUPER_ADMIN']
