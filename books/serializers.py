from rest_framework import serializers
from .models import Book, MyBookList

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'image']

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBookList
        fields = ['books']