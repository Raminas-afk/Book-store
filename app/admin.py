from django.contrib import admin
from .models import Book, Category, Order, Cart
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['title', 'author', 'quantity', 'price']


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['order_id', 'customer', 'date', 'price', 'shipped_status']


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)
