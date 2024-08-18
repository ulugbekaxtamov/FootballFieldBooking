from rest_framework import permissions
from django.contrib.auth.models import Group


class CreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated:
            admin_group = Group.objects.get(name='Admin')
            owner_group = Group.objects.get(name='Owner')
            if admin_group in request.user.groups.all() or owner_group in request.user.groups.all():
                return True
        return False


class UpdateDeleteObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        admin_group = Group.objects.get(name='Admin')
        if request.user in admin_group.user_set.all() or obj.owner == request.user:
            return True
        return False
