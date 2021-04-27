from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    book_image = models.TextField()

    def __str__(self):
        return f"title: {self.title}, author: {self.author}, description: {self.description}, book_image: {self.book_image}"

class MyBookList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='book_list')
    books = models.ManyToManyField(Book, related_name='book_lists', blank=True)

    @receiver(post_save, sender=User)
    def create_user_booklist(sender, instance, created, **kwargs):
        if created:
            MyBookList.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_booklist(sender, instance, **kwargs):
        instance.book_list.save()

class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='wish_list')
    books = models.ManyToManyField(Book, related_name='wish_lists', default=[], blank=True)
    
    @receiver(post_save, sender=User)
    def create_user_wishlist(sender, instance, created, **kwargs):
        if created:
            WishList.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_wishlist(sender, instance, **kwargs):
        instance.wish_list.save()

class Swap(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='proposed_swaps')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='received_swaps')
    book1 = models.ForeignKey(Book, on_delete=models.CASCADE,  related_name='proposed_swaps')
    book2 = models.ForeignKey(Book, on_delete=models.CASCADE,  related_name='received_swaps')
    status = models.CharField(max_length=255, default="proposed")








