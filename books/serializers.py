from rest_framework import serializers
from .models import Book, MyBookList, WishList

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'image']

class BookListSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = MyBookList
        fields = ['user', 'books']

    def create(self, validated_data):
        print(validated_data)
        book_validated_data = validated_data.pop('books')
        print(book_validated_data)
        book_list = MyBookList.objects.create(**validated_data)
        book_set_serializer = self.fields['books']
        for book_data in book_validated_data:
            Book.objects.create(**book_data)
        books = book_set_serializer.create(book_validated_data)
        return book_list

    def update(self, instance, validated_data):
        print(validated_data)
        book_validated_data = validated_data.pop('books')
        print(book_validated_data)
        book_list = MyBookList.objects.create(**validated_data)
        book_set_serializer = self.fields['books']
        for book_data in book_validated_data:
            Book.objects.create(**book_data)
        books = book_set_serializer.create(book_validated_data)
        return book_list

class WishListSerializer(serializers.ModelSerializer):
    # books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = WishList
        fields = ['user', 'books']

    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     book_validated_data = validated_data.pop('books')
    #     print(book_validated_data)
    #     book_list = MyBookList.objects.create(**validated_data)
    #     book_set_serializer = self.fields['books']
    #     for book_data in book_validated_data:
    #         Book.objects.create(**book_data)
    #     books = book_set_serializer.create(book_validated_data)
    #     return book_list