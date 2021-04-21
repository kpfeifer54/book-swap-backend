from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return f"title: {self.title}, author: {self.author}, description: {self.description}, image: {self.image}"

class MyBookList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='book_lists')
    books = models.ManyToManyField(Book, related_name='book_lists')

class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='wish_lists')
    books = models.ManyToManyField(Book, related_name='wish_lists')
    
    @receiver(post_save, sender=User)
    def create_user_wishlist(sender, instance, created, **kwargs):
        if created:
            WishList.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_wishlist(sender, instance, **kwargs):
        instance.wish_lists.save()







