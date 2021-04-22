from django.urls import path, include
from .views import BookViewSet, BookListViewSet, WishListViewSet, SwapViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'book_list', BookListViewSet, basename='booklist')
router.register(r'wish_list', WishListViewSet, basename='wishlist')
router.register(r'swap', SwapViewSet, basename='swap')
urlpatterns = router.urls