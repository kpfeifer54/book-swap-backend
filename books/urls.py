from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BookViewSet, basename='book')
urlpatterns = router.urls