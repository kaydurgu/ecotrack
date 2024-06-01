from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer, UserCreateSerializer
# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Admin').exists():
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        return super().post(request, *args, **kwargs)