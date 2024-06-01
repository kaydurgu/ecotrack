from django.shortcuts import render
from rest_framework import permissions


# Create your views here.

class IsInGroup(permissions.BasePermission):
    group_name = None
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.groups.filter(name=self.group_name).exists()
        return False

class IsAdminUser(IsInGroup):
    group_name = 'Admin'
class IsWorkerUser(IsInGroup):
    group_name = 'Worker'

