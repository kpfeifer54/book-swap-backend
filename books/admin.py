from django.contrib import admin
from .models import Book, MyBookList, WishList

admin.site.register(Book)
admin.site.register(MyBookList)
admin.site.register(WishList)
