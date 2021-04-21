from django.urls import path, include
from .views import BookViewSet, BookList, WishListViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('my-book-list/', BookList.as_view())
# ]

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'my-book-list', BookList, basename='booklist')
router.register(r'wish-list', WishListViewSet, basename='wishlist')
# router.register(r'my-book-list', BookList.as_view(), basename='booklist')
urlpatterns = router.urls