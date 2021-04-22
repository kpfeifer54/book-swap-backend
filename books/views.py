from .models import Book, MyBookList, WishList, Swap
from .serializers import BookSerializer, BookListSerializer, WishListSerializer, SwapSerializer
from rest_framework import viewsets
from rest_framework import generics
from django.db.models import Q

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListViewSet(viewsets.ModelViewSet):
    queryset = MyBookList.objects.all()
    serializer_class = BookListSerializer

class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

class SwapViewSet(viewsets.ModelViewSet):
    queryset = Swap.objects.all()
    serializer_class = SwapSerializer

    def get_queryset(self):
        user = self.request.user
        return Swap.objects.filter(Q(user1=user) | Q(user2=user))
