from django.contrib import admin
from .models import Book, Category, Order, Cart
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['title', 'author', 'quantity', 'price']


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Cart)
