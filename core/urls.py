from django.urls import path
from .views import current_user, UserList, UserListViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
]
router = DefaultRouter()
router.register(r'user-list', UserListViewSet, basename='user_list')
urlpatterns += router.urls