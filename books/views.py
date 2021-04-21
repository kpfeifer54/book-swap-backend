from .models import Book, MyBookList, WishList
from .serializers import BookSerializer, BookListSerializer, WishListSerializer
from rest_framework import viewsets
from rest_framework import generics

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(viewsets.ModelViewSet):
    queryset = MyBookList.objects.all()
    serializer_class = BookListSerializer

    def get_queryset(self):
        user = self.request.user
        return MyBookList.objects.filter(user=user)

class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
