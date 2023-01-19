from django.shortcuts import render, redirect
from .models import Book, Cart, Order
from django.contrib import messages

# Create your views here.


def homepage(request):
    books = Book.objects.all()
    return render(request, "app/index.html", {
        "books": books
    })


def sort_by_category(request, category):
    books = Book.objects.filter(category=category)
    return render(request, "app/index.html", {
        "books": books
    })


def sort_bestsellers(request):
    books = Book.objects.filter(is_bestselling=True)
    return render(request, "app/index.html", {
        "books": books
    })


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    print(book.cover.name)
    return render(request, "app/book_detail.html", {
        "book": book,
    })


def my_cart(request):
    if request.method == "GET":
        instance = Cart.objects.get(customer=request.user.profile)
        cart_books = instance.books.all()
        total_price = instance.get_total_price()
        return render(request, "app/my_cart.html", {
            "cart_books": cart_books,
            "total_price": total_price

        })


def add_to_cart(request, slug):
    book = Book.objects.get(slug=slug)
    stock = book.quantity
    if stock >= 1:
        cart = Cart.objects.get(customer=request.user.profile)
        cart.books.add(book)
        return redirect("my-cart")
    else:
        messages.error(request, f"{book.title} is currently out of stock.")
        return redirect("book-detail", slug)


def remove_from_cart(request, slug):
    cart = Cart.objects.get(customer=request.user.profile)
    book = Book.objects.get(slug=slug)
    cart.books.remove(book)
    return redirect("my-cart")


def place_order(request):
    customer = request.user.profile
    customer_cart = Cart.objects.get(customer=customer)
    total_price = customer_cart.get_total_price()
    new_order = Order.objects.create(
        customer=customer,
        price=total_price,
    )
    new_order.books.set(customer_cart.books.all())
    new_order.save()
    for book in customer_cart.books.all():  # Removes items from cart after order
        customer_cart.books.remove(book)
    messages.success(request, "Your order is done!")
    return redirect("my-cart")
