from django.urls import path
from . import views

urlpatterns = [
    path('title/', views.title, name='title_url'),
    path('get_all_books/', views.all_books, name="all_books_url"),
    path('books/<int:id>/', views.book_info, name="book_info_url"),
]