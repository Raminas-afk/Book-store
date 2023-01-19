from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('book/<str:slug>', views.book_detail, name="book-detail"),
    path('sort/<str:category>', views.sort_by_category, name="sort-category"),
    path('bestsellers', views.sort_bestsellers, name='sort-bestsellers'),
    path('my_cart', views.my_cart, name="my-cart"),
    path('add-to-cart/<str:slug>', views.add_to_cart, name="add-to-cart"),
    path('remove_from_cart/<str:slug>',
         views.remove_from_cart, name="remove-from-cart"),
    path('place_order', views.place_order, name="place-order")
]
