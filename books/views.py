from .models import Book, MyBookList
from .serializers import BookSerializer, BookListSerializer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListViewSet(viewsets.ModelViewSet):
    queryset = MyBookList.objects.all()
    serializer_class = BookListSerializer
