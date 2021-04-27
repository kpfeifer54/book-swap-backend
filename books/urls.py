from django.urls import path, include
from .views import BookViewSet, BookListViewSet, WishListViewSet, SwapViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'book_list', BookListViewSet, basename='booklist')
router.register(r'wish_list', WishListViewSet, basename='wishlist')
router.register(r'swap', SwapViewSet, basename='swap')
urlpatterns = router.urls

# class NestedDefaultRouter(NestedRouterMixin, DefaultRouter): 
#     pass

# router = NestedDefaultRouter()
# # router.register(r'wish_list', WishListViewSet, basename='wishlist')
# list_router = router.register(r'wish_list', WishListViewSet)
# list_router.register(r'books', BookViewSet, basename="wishlist", parents_query_lookups=["wishlist"])
# urlpatterns = router.urls