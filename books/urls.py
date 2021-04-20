from django.urls import path, include
from .views import BookViewSet, BookListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'my-book-list', BookListViewSet, basename='booklist')
urlpatterns = router.urls