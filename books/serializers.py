from rest_framework import serializers
from .models import Book, MyBookList, WishList, Swap

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'book_image', 'id']

class BookListSerializer(serializers.ModelSerializer):
    # books = BookSerializer(many=True, read_only=True)
    # user = serializers.StringRelatedField(many=True)

    class Meta:
        model = MyBookList
        fields = ['user', 'books']

class WishListSerializer(serializers.ModelSerializer):
    # books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = WishList
        fields = ['user', 'books']

class SwapSerializer(serializers.ModelSerializer):

    class Meta:
        model = Swap
        fields = ['user1', 'user2', 'book1', 'book2', 'status', 'id']