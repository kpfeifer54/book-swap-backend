from django.contrib import admin
from .models import Book, MyBookList, WishList, Swap

admin.site.register(Book)
admin.site.register(MyBookList)
admin.site.register(WishList)
admin.site.register(Swap)
