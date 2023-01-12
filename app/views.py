from django.shortcuts import render
from .models import Book
# Create your views here.


def homepage(request):
    books = Book.objects.all()
    print(books)
    return render(request, "app/index.html", {
        "books": books
    })


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    print(book.cover.name)
    return render(request, "app/book_detail.html", {
        "book": book
    })
