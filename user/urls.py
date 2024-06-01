from django.urls import path, include

from .views import UserListView, UserDetailView, UserCreateView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('auth/', include('rest_framework.urls')),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('create/', UserCreateView.as_view(), name='worker-create'),
]