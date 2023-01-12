from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('book/<str:slug>', views.book_detail, name="book-detail"),
    path('sort/<str:category>', views.sort_by_category, name="sort-category"),
    path('bestsellers', views.sort_bestsellers, name='sort-bestsellers')
]
