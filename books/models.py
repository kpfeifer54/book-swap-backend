from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.title

class MyBookList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='book_lists')
    books = models.ManyToManyField(Book, related_name='book_lists')

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='wish_lists')
    books = models.ManyToManyField(Book, related_name='wish_lists')





