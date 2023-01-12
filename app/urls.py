from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('book/<str:slug>', views.book_detail, name="book-detail")
]
